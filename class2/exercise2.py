from netmiko import Netmiko
from getpass import getpass
from datetime import datetime

password = getpass()
devices = {'host': 'nxos2.lasthop.io', 'username': 'pyclass', 'password': '88newclass', 'device_type': 'cisco_nxos', 'session_log': 'logging.txt', 'global_delay_factor':2}

ssh_conn = Netmiko(**devices)
print(ssh_conn.find_prompt())

start_time = datetime.now()
output_delay_2 = ssh_conn.send_command('show lldp neighbors detail')
end_time = datetime.now()

print(output_delay_2)
print('-' *79)
print(f"Execution Time :{end_time} : {start_time}")
print('-' *79)
start_time2 = datetime.now()
output_delay_8 = ssh_conn.send_command('show lldp neighbors detail', delay_factor=8)
end_time2 = datetime.now()
print(output_delay_8)
print('-' *79)
print(f"Execution Time for delay of 2 :{end_time} : {start_time}")
print('-' *79)
print(f"Execution Time for delay of 8:{end_time2} : {start_time2}")
print('-' *79)

