#!/usr/bin/python

"""
find known MAC-Adresses on netonix switches

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

The primary goal of this script is to find known devices(e.g. Wifi APs) in the mac-address table. 
It compairs all MACs against a list of known devices and assumes that all ports with 
maximum 2 known devices are edge port. Those edge-ports with the mac and ip information 
are return as the result.

This filter assumes a very specific environment:
 - the known adress file must be in format of the mikrotik static lease configuration export
 - it assumes all devices with mac "80:5e:c0:*:*:*" as known devices(voip phones) 
 - the switch IP is prepended to each output line
 - username and known mac file are hard-coded
 """
 
import netonix_api
import json
import sys
import getpass
import traceback
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def read_file(f):
	res={}
	f=open(f)
	for l in f:
		a=l.split(" ")
		ip=""
		mac=""
		comment=""
		for i in a:
			if(i.startswith("address=")):
				ip=i.split("=")[1].strip()
			if(i.startswith("mac-address=")):
				mac=i.split("=")[1].strip()
			if(i.startswith("comment=")):
				comment=i.split("=")[1].strip()
		if(mac!=""):
			res[mac.lower()]=(ip.lower(),mac.lower(),comment)
	return res 
	

if __name__ == '__main__':
	ip=sys.argv[1]
	pw= getpass.getpass()
	macs=read_file("190408-leases.rsc")
	username="admin"
	target=[]
	try:
		with open(ip) as f:
			for line in f:
				target.append(line.strip())
	except:
		if(len(target)==0):
			target.append(ip)
		else:
			traceback.print_exc()
			exit()
	print("%s\t%s\t%s\t%s\t%s"%("Switch","Port","MAC","IP DHCP","IP Switch"))
	for ip in target:
		a=netonix_api.Netonix()
		sys.stderr.write("get macs from %s"%ip)
		try:
			a.open(ip,username,pw)
			mac_all={}
			for i in range(3):
				a.getMAC()
				time.sleep(0.1)
				for m in a.mac:
					mac_address=m["MAC"].replace("-",":").lower()
					mac_all[mac_address]=m
		except:
			traceback.print_exc(file=sys.stderr)
			continue
		res={}
		for pm in mac_all.keys():
				
			current_mac=mac_all[pm]
			try:
				current_mac["AP_IP"]=macs[pm][0]
			except:
				if(not pm.startswith("80:5e:c0:")):
					continue
				current_mac["AP_IP"]="unknown"
			try:
				res[current_mac["Port"]][pm]=current_mac
			except:
				res[current_mac["Port"]]={pm:current_mac}
		for a in res.keys():
			if(len(res[a])<3):
				for ml in res[a].keys():
					i=res[a][ml]
					print("%s\t%s\t%s\t%s\t%s"%(ip,i["Port"],i["MAC"].replace("-",":").lower(),i["AP_IP"],i["Last_IP"]))
