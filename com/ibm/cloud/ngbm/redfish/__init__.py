import json
import os

print(os.environ['REDFISH_HOME']+'/etc/redfish.json')
with open(os.environ['REDFISH_HOME']+'/etc/redfish.json') as f:
  cfg = json.load(f)

target=cfg["target"]
defaultPrefix=cfg["defaultPrefix"]
username=cfg["username"]
password=cfg["password"]
authentication=cfg["authentication"]