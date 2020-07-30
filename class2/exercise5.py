import os
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from datetime import datetime

#password = getpass()
hosts = ["cisco1.lasthop.io", "cisco2.lasthop.io"]

for host in hosts:
    device = {'host': host, 'username': 'pyclass', 'password': '88newclass', 'device_type': 'cisco_ios', 'session_log': 'logging.txt', 'fast_cli': True}
    ssh_conn = Netmiko(**device)
    print(ssh_conn.find_prompt())

    print("Configuration of vlan 100-105")
    sent_vlan = ssh_conn.send_config_from_file("vlans.txt")
    print("Commit")
    write_conf = ssh_conn.save_config()
    print(write_conf)





