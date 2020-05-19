import json
import os

print("Configuration File: " + os.environ['REDFISH_HOME']+'/etc/redfish.json')
with open(os.environ['REDFISH_HOME']+'/etc/redfish.json') as f:
  cfg = json.load(f)

#REDFISH TARGET
target : str =cfg["target"]
defaultPrefix : str =cfg["defaultPrefix"]
username : str =cfg["username"]
password : str =cfg["password"]
authentication : str =cfg["authentication"]

#REDFISH SERVICES
odataIdKey: str = "@odata.id"
uriKey: str = "URI"
hostKey: str = "Host"
pathKey: str = "Path"
oemKey: str = "Oem"
supermicroKey: str = "Supermicro"
actionsKey : str = "Actions"
consoleKey: str = "IKVM"

virtualMediaKey: str = "VirtualMedia"
virtualMediaMembersKey : str = "Members"
virtualMediaMembersCountKey : str = "Members@odata.count"
virtualMediaTargetKey : str = "target"
virtualMediaConfigKey : str = "VirtualMediaConfig"
virtualMediaMountKey: str = "#IsoConfig.Mount"
virtualMediaUnmountKey: str = "#IsoConfig.UnMount"

bootFromNone = "None"
bootFromPxe = "Pxe"
bootFromFloppy = "Floppy"
bootFromCd = "Cd"
bootFromUsb = "Usb"
bootFromHdd = "Hdd"
bootFromBiosSetup = "BiosSetup"

powerStatusOn : str = "On"
powerStatusOff : str = "Off"

managers: str = "/redfish/v1/Managers/1/"
systems: str = "/redfish/v1/Systems/1/"
bios: str = "redfish/v1/Systems/1/Bios"

resetActionURI : str = systems + actionsKey + "/ComputerSystem.Reset"
resetType : str = "ResetType"
resetActionOn : dict = {resetType:"On"}
resetActionForceOn : dict = {resetType:"ForceOn"}
resetActionOff : dict = {resetType: "GracefulShutdown"}
resetActionForceOff : dict = {resetType:"ForceOff"}
resetActionRestart : dict = {resetType: "GracefulRestart"}
resetActionForceRestart : dict = {resetType:"ForceRestart"}