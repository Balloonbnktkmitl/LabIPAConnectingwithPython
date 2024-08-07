from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
import yaml
import os

loader = FileSystemLoader("templates")
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = env.get_template("router-nat.j2")

with open("data/router-nat.yml") as f:
    config = yaml.safe_load(f)

config_output = template.render(config)

device = {
    'device_type': 'cisco_ios',
    'host': '172.31.103.4',
    'username': os.environ.get('TELNET_USER'),
    'password': os.environ.get('TELNET_PASSWORD')   
}

connection = ConnectHandler(**device)
connection.enable()
output = connection.send_config_set(config_output.split('\n'))
print(output)
connection.save_config()
connection.disconnect()
