#!/usr/bin/python
#
"""
run commands on netonix api from ansible

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

DOCUMENTATION = """
---
module: netonix_command
author: "shrank (info@murxs.ch)"
short_description: run commands Netonix WISP Switch WebAPI
description:
- run commands on Netonix WISP Switch WebAPI
options: 

"""

EXAMPLES = r"""

REMARK: use this module in combination with the "local_action" module

- hosts: all
  gather_facts: False
  connection: network_cli
  vars:
      ansible_network_os: ios

  tasks:
  - name: get known devices from mac table
    block:
     - local_action:
         module: netonix_command
         username: "{{ ansible_user}}"
         password: "{{ ansible_password}}"
         target: "{{ inventory_hostname }}"
         command:  mac
       register: output
     - local_action: copy content='{{output.output | find_ap(inventory_hostname,'known_devices.list') }}' dest="{{output_dir}}/{{ inventory_hostname }}.mac"
     
  tasks:
  - name: backup running config
    block:
      - local_action:
          module: netonix_command
          username: "{{ ansible_user}}"
          password: "{{ ansible_password}}"
          target: "{{ inventory_hostname }}"
          command: config
        register: output
      - local_action: copy content='{{output.config | to_nice_json(indent=4)}}' dest="{{backup_dir}}/{{ inventory_hostname }}.conf"
     
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.common.utils import ComplexList
from ansible.module_utils.network.common.parsing import Conditional
from ansible.module_utils.six import string_types
import netonix_api
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def main():
	"""main entry point for module execution
	"""
	argument_spec = dict(
		target=dict(type='str', required=True),
		username=dict(type='str', required=True),
		password=dict(type='str', required=True),
		command=dict(type='str', required=True)
	)


	module = AnsibleModule(argument_spec=argument_spec,
									supports_check_mode=True)

	result = {'changed': False}
	target= module.params["target"]
	password= module.params["password"]
	username= module.params["username"]
	command= module.params["command"]
	warnings = list()
	a=netonix_api.Netonix()
	try:
		a.open(target,username,password)
	except:
		module.fail_json(msg="Unexpected error: " + str(e))
		return
	if(command=="mac"):
		mac_all={}
		for i in range(3):
			a.getMAC()
			for m in a.mac:
				mac_address=m["MAC"].replace("-",":").lower()
				mac_all[mac_address]=m
		result.update({
		'changed': True,
		'output': mac_all
		})
	elif(command=="config"):
		try:
			a.getConfig()
		except:
			module.fail_json(msg="Unexpected error: " + str(e))
			return
		result.update({
			'changed': True,
			'config': a.config
		})
	else:
		module.fail_json(msg="Unknown command: " + command)
		return
	module.exit_json(**result)


if __name__ == '__main__':
	main()
