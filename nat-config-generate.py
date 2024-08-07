from jinja2 import Environment, FileSystemLoader
import yaml

loader = FileSystemLoader("templates")
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = env.get_template("router-nat.j2")

with open("data/router-nat.yml") as f:
    routers = yaml.safe_load(f)

with open("config/router-nat.txt", "w") as f:
    f.write(template.render(routers))

