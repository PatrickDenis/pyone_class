import jinja2

dict_var = {'peer1_ip': '10.10.10.1', 'peer1_as': '20'}

template = """
feature bgp
router bgp 10
    address-family ipv4 unicast
        network 10.10.10.0/24
    neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
        update-source lo0
        ebgp-multihop 2
        address-family ipv4 unicast
"""

t = jinja2.Template(template)
print(t.render(dict_var))

