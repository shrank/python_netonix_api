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
import time
import json

class Netonix():
    def __init__(self):
        self.ip=None
        self.s=None
        self.url={}
        self.url["login"]="/index.php"
        self.url["backup"]="/api/v1/backup"
        self.url["config"]="/api/v1/config"
        self.url["apply"]="/api/v1/apply"
        self.url["confirm"]="/api/v1/applystatus"
        self.url["reboot"]="/api/v1/reboot"
        self.url["restore"]="/api/v1/restore"
        self.url["mac"]="/api/v1/mactable"
        self.url["status"]="/api/v1/status/30sec"
        self.url["id"]="/api/v1/bootid"
        self.config={}
        self.mac={}
        self.status={}
        self.id=""
        pass
    def open(self,ip,user,password):
        self.ip=ip
        self.s = requests.session()
        self.s.verify=False
        data={}
        data["username"]=user
        data["password"]=password
        r = self.s.post("https://"+self.ip+self.url["login"], data)
        if("Invalid username or password" in r.text):
            raise Exception("Invalid username or password")
    def getConfig(self):
        r = self.s.get("https://"+self.ip+self.url["config"])
        result=r.json()
        if("Config_Version" in result):
            self.config=result
    def putConfig(self):
        raise Exception("the putConfig method is still untested.")
        r = self.s.post("https://"+self.ip+self.url["config"], json=self.config)
        print(r.json())
        r = self.s.post("https://"+self.ip+self.url["apply"])
        time.sleep(2)
        r = self.s.post("https://"+self.ip+self.url["confirm"])
        return r.json()
    def backup(self,output):
        r = self.s.get("https://"+self.ip+self.url["backup"]+"/"+self.ip)
        if(r.status_code != requests.codes.ok):
            raise Exception("Backup Request Failed")
        newFile = open(output, "wb")
        newFile.write(r.content)
        newFile.close()
    def restore(self,i):
        raise Exception("the restore method is still untested.")
        newFile = open(i, "rb")
        data=""
        for a in newFile:
            data+=a
        newFile.close()
        r = self.s.post("https://"+self.ip+self.url["restore"],data)
        print(r.json())
        if(r.status_code != requests.codes.ok):
            raise Exception("Restore Request Failed")
        r = self.s.get("https://"+self.ip+self.url["reboot"])
        return r.json()
    def getMAC(self):
        r = self.s.get("https://"+self.ip+self.url["mac"])
        self.mac=r.json()["MACTable"]
    def getID(self):
        r = self.s.get("https://"+self.ip+self.url["id"]+"?_=%d"%time.time())
        self.id=r.json()["BootID"]
    def getStatus(self):
        if(self.id==""):
            self.getID()
        r = self.s.get("https://"+self.ip+self.url["status"]+"?%s&_=%d"%(self.id,time.time()))
        self.status=r.json()

if __name__ == '__main__':
    import getpass
    import traceback
    import urllib3
    import sys
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    ip=str(input("switch ip:"))
    user=str(input("user:"))
    pw= getpass.getpass("password:")
    n=Netonix()
    n.open(ip,user,pw)
    n.getStatus()
    print(json.dumps(n.status,indent=4))
