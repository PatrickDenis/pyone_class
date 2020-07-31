import os
from netmiko import ConnectHandler
from getpass import getpass


def display_output(output):
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()

    nxos1 = {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
    }
    nxos2 = {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
    }

for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    print(ssh_conn.find_prompt())

    