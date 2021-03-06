import jinja2

network_routes = ['10.10.10.0/24', '20.20.20.0/24', '30.30.30.0/24']
bgp_dict = {'peer1_ip': '10.10.10.1', 'peer1_as': '20','network_routes': network_routes,'local_as': '30'}

#template_file = 'template.j2'
with open('template_loop.j2') as f:
    bgp_template = f.read()

t = jinja2.Template(bgp_template)
print(t.render(bgp_dict))

