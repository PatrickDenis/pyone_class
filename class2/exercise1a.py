from netmiko import Netmiko
from getpass import getpass

password = getpass()
devices = {'host': 'cisco4.lasthop.io', 'username': 'pyclass', 'password': password, 'device_type': 'cisco_xe', 'session_log': 'logging.txt', "fast_cli": True}

ssh_conn = Netmiko(**devices)
print(ssh_conn.find_prompt())

ipv4 = '8.8.8.8'

output  = ssh_conn.send_command_timing("ping", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command_timing(ipv4, strip_prompt=False, strip_command=False)
output += ssh_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command_timing("\n", strip_prompt=False, strip_command=False)
ssh_conn.disconnect()

print(output)



