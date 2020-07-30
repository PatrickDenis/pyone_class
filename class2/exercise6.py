import os
import time
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from datetime import datetime

password = getpass()
devices = {'host': 'cisco4.lasthop.io', 'username': 'pyclass', 'password': password, 'device_type': 'cisco_xe', 'session_log': 'my_output.txt', 'fast_cli': True, 'secret': password}

ssh_conn = Netmiko(**devices)
print("-" *79)
print("Execution of the command prompt :")
print("-" *79)
print(ssh_conn.find_prompt())
print("-" *79)
print("Execution the config_mode:")
print("-" *79)
ssh_conn.config_mode()
print(ssh_conn.find_prompt())
print("-" *79)
print("Execution the exit_config_mode:")
print("-" *79)
ssh_conn.exit_config_mode()
print(ssh_conn.find_prompt())
print("-" *79)
print("Execution the write_channel:")
print("-" *79)
ssh_conn.write_channel('disable')
print(ssh_conn.find_prompt())
print("-" *79)
print("Execution the time sleep command:")
time.sleep(2)
print("-" *79)
print("Execution the read_channel:")
print("-" *79)
ssh_conn.read_channel()
print(ssh_conn.find_prompt())
print("-" *79)
print("Execution the enable mode:")
print("-" *79)
ssh_conn.read_channel()
ssh_conn.enable()
print(ssh_conn.find_prompt())
print("-" *79)
