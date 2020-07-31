import os
from netmiko import Netmiko
from getpass import getpass
from pprint import pprint
from datetime import datetime

#password = getpass()
devices = {'host': 'cisco3.lasthop.io', 'username': 'pyclass', 'password': '88newclass', 'device_type': 'cisco_xe', 'session_log': 'logging.txt', 'fast_cli:True'}

ssh_conn = Netmiko(**devices)
print(ssh_conn.find_prompt())

commands = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
verify_command = "ping google.com"

start_time = datetime.now()
push1 = ssh_conn.send_config_set(commands)
print(push1)
push2 = ssh_conn.send_command(verify_command)

if "!!" in push2:
    print("Ping Successful:")
    print(f"Result :{push2}")
else:
    print("Not Working FIX IT")
    
end_time = datetime.now()
print(f"Execution Time for delay of 2 :{end_time} : {start_time}")




