#!/usr/bin/env python3
"""
Python class to access Netonix® WISP Switch WebAPI

** NEITHER THIS CODE NOR THE AUTHOR IS ASSOCIATED WITH NETONIX® IN ANY WAY.**

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

import requests
from requests.exceptions import Timeout
from copy import deepcopy
import time
import json
try:
    from deepdiff import DeepDiff
    DIFF = True
except:
    DIFF = False

class Netonix():
    def __init__(self):
        self.ip = None
        self.s = None
        self.url = {}
        self.url["login"] = "/index.php"
        self.url["backup"] = "/api/v1/backup"
        self.url["config"] = "/api/v1/config"
        self.url["apply"] = "/api/v1/apply"
        self.url["confirm"] = "/api/v1/applystatus"
        self.url["reboot"] = "/api/v1/reboot"
        self.url["restore"] = "/api/v1/restore"
        self.url["mac"] = "/api/v1/mactable"
        self.url["status"] = "/api/v1/status/30sec"
        self.url["id"] = "/api/v1/bootid"
        self.url["update"] = "/api/v1/uploadfirmware"
        self.url["doupdate"] = "/api/v1/upgradefirmware"
        self.config = {}
        self.orig_config = None
        self.mac = {}
        self.status = {}
        self.id = ""

    def _get(self, url, params=None, timeout=15, **kwargs):
        full_url = "https://"+self.ip+self.url[url]
        return self.s.get(full_url, params=params, timeout=timeout, **kwargs)

    def _post(self, url, data=None, json=None, timeout=15, **kwargs):
        full_url = "https://"+self.ip+self.url[url]
        return self.s.post(
            full_url,
            data=data,
            json=json,
            timeout=timeout,
            **kwargs
        )

    @staticmethod
    def _merge_by_key(old, new, key="Number", append=True):
        for item in new:
            found = False
            for old_item in old:
                if(key not in old_item):
                    continue
                if(old_item[key] != item[key]):
                    continue
                old_item.update(item)
                found = True
                break
            if(found is False):
                if(append is True):
                    old_item.append(new)
                else:
                    raise LookupError()

    def open(self, ip, user, password):
        self.ip = ip
        self.s = requests.session()
        self.s.verify = False
        data = {}
        data["username"] = user
        data["password"] = password
        r = self._post("login", data)
        if("Invalid username or password" in r.text):
            raise Exception("Invalid username or password")

    def getConfig(self):
        r = self._get("config")
        result = r.json()
        if("Config_Version" in result):
            self.config = result

    def putConfig(self):
        r = self._post("config", json=self.config)
        try:
            r = self._post("apply")
        except Timeout:
            pass
        self.ip = self.config["IPv4_Address"]
        for a in range(5):
            try:
                r = self._post("confirm")
            except Timeout:
                continue
            break
        if(r.status_code != requests.codes.ok):
            raise Exception("Config Confirm Request Failed")
        # return r.json()

    def backup(self, output):
        r = self.s.get("https://"+self.ip+self.url["backup"]+"/"+self.ip)
        if(r.status_code != requests.codes.ok):
            raise Exception("Backup Request Failed")
        newFile = open(output, "wb")
        newFile.write(r.content)
        newFile.close()

    def restore(self, i):
        raise Exception("the restore method is still untested.")
        newFile = open(i, "rb")
        data = ""
        for a in newFile:
            data += a
        newFile.close()
        r = self._post("restore", data)
        print(r.json())
        if(r.status_code != requests.codes.ok):
            raise Exception("Restore Request Failed")
        r = self._get("reboot")
        return r.json()

    def getMAC(self):
        r = self._get("mac")
        if(r.status_code != requests.codes.ok):
            raise Exception("Action failed")
        self.mac = r.json()["MACTable"]

    def getID(self):
        r = self._get("id", params={"_": time.time()})
        if(r.status_code != requests.codes.ok):
            raise Exception("Action failed")
        self.id = r.json()["BootID"]

    def getStatus(self):
        if(self.id == ""):
            self.getID()
        r = self.s.get("https://"+self.ip+self.url["status"]+"?%s&_=%d" % (self.id, time.time()))
        if(r.status_code != requests.codes.ok):
            raise Exception("Action failed")
        self.status = r.json()

    def update(self, i):
        data = ""
        with open(i, mode='rb') as file:  # b is important -> binary
            data = file.read()
        r = self._post("update", data)
        if(r.status_code != requests.codes.ok):
            raise Exception("Firmware Upload Failed")
        r = self._get("doupdate")
        if(r.status_code != requests.codes.ok):
            raise Exception("Update Request Failed")

    def mergeConfig(self, config):
        self.orig_config = deepcopy(self.config)

        for k, v in config.items():
            if(k == "Ports"):
                self._merge_by_key(self.config[k], v, key="Number")
                continue
            if(k == "LACP"):
                self._merge_by_key(self.config[k], v, key="Port")
                continue
            if(k == "VLANs"):
                self._merge_by_key(self.config[k], v, key="ID")
                continue
            if(type(v) is dict):
                continue
            if(type(v) is list):
                self.config[k] += v
                continue
            self.config[k] = v

    def replaceConfig(self, config):
        self.orig_config = deepcopy(self.config)

        if("Config_Version" in config):
            del config["Config_Version"]
        self.config.update(config)

    def getDiff(self):
        if(self.orig_config is None):
            return {}
        if(DIFF is False):
            raise ImportError("Missing DeepDiff Module")
        return DeepDiff(
            self.orig_config,
            self.config,
            exclude_paths="root['Config_Version']"
            )


if __name__ == '__main__':
    import getpass
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    ip = str(input("switch ip:"))
    user = str(input("user:"))
    pw = getpass.getpass("password:")
    n = Netonix()
    n.open(ip, user, pw)
    n.getStatus()
    print(json.dumps(n.status, indent=4))
