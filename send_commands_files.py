#!/usr/local/bin/python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
    "fast_cli": True,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

pre_check = net_connect.send_config_from_file(config_file="pre_check.txt")
roll_out = net_connect.send_config_from_file(config_file="roll_out.txt")
post_check = net_connect.send_config_from_file(config_file="post_check.txt")

with open("pre_check.{}.txt".format(device1['host']), "a") as f:
    f.write(pre_check)

with open("roll_out.{}.txt".format(device1['host']), "a") as f:
    f.write(roll_out)

with open("post_check.{}.txt".format(device1['host']), "a") as f:
    f.write(post_check)


net_connect.disconnect()
