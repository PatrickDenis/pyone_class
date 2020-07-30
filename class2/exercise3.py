import os
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

#password = getpass()
devices = {'host': 'cisco4.lasthop.io', 'username': 'pyclass', 'password': '88newclass', 'device_type': 'cisco_ios', 'session_log': 'logging.txt'}

ssh_conn = Netmiko(**devices)
print(ssh_conn.find_prompt())

show_version = ssh_conn.send_command('show version', use_textfsm=True)
show_lldp = ssh_conn.send_command('show lldp neighbor', use_textfsm=True)

print(f"The device {devices['host']} is connected to port {show_lldp[0]['neighbor_interface']}")










