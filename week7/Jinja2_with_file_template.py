import jinja2

bgp_vars = {'peer1_ip': '10.10.10.1', 'peer1_as': '20'}

#template_file = 'template.j2'
with open('template.j2') as f:
    bgp_template = f.read()

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))

