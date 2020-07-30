from netmiko import Netmiko
from getpass import getpass

password = getpass()
devices = {'host': 'cisco4.lasthop.io', 'username': 'pyclass', 'password': password, 'device_type': 'cisco_xe', 'session_log': 'logging.txt', "fast_cli": True}

ssh_conn = Netmiko(**devices)
print(ssh_conn.find_prompt())

ipv4 = '8.8.8.8'

output  = ssh_conn.send_command("ping", expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command("\n", expect_string=r"Target", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command(ipv4, expect_string=r"Repeat", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command("\n", expect_string=r"Datagram", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command("\n", expect_string=r"Timeout", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command("\n", expect_string=r"Extended", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command("\n", expect_string=r"Sweep", strip_prompt=False, strip_command=False)
output += ssh_conn.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)
ssh_conn.disconnect()

print(output)