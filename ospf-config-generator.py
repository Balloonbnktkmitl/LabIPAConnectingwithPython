from jinja2 import Environment, FileSystemLoader
import yaml

loader = FileSystemLoader("templates")
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = env.get_template("router-ospf.j2")

with open("data/router-ospf.yml") as f:
    routers = yaml.safe_load(f)

for router in routers:
    router_config = "config/" + router['management_ip'] + "-exercise-ospf.txt"
    with open(router_config, "w") as f:
        f.write(template.render(router))

