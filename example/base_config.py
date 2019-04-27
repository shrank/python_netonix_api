#!/usr/bin/python

"""
Push a default config to a switch

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


Description:

This script can get the configuration from a device and push it to other devices as a default config.
The script automatically changes the hostname to the 2 last octets of the IP. Furthermore it preserves
all port labels that read "BAD"(My friends like to break ports). 

get config:
python base_config.py get 10.10.10.1 config-template.json

push config:
python base_config.py push 10.10.10.1 config-template.json


 """
 
import netonix_api
import json
import sys
import getpass
import traceback
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
	filename=sys.argv[3]
	ip=sys.argv[2]
	cmd=sys.argv[1]
	pw= getpass.getpass()
	username="admin"
	n=netonix_api.Netonix()
	n.open(ip,username,pw)
	n.getConfig()
	if(cmd=="get"):
		with open(filename, 'w') as fp:
			json.dump(n.config, fp,indent=4)
			exit(1)
	elif(cmd=="push"):
		with open(filename) as json_data:
			default = json.load(json_data)
		default["IPv4_Address"]=ip
		a=ip.split(".")
		default["Switch_Name"]="%s.%s"%(a[2],a[3])
		default["Config_Version"]=n.config["Config_Version"]
		i=0
		for a in n.config["Ports"]:
			i+=1
			print("%d:\t%s"%(i,a["Name"]))
			if(a["Name"].lower()=="bad"):
				default["Ports"][i-1]["Name"]="BAD"
				default["Ports"][i-1]["PoE"]="Off"
		n.config=default
		n.putConfig()
	else:
		print("Command %s unkown"%cmd)			
