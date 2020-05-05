from com.ibm.cloud.ngbm.redfish.ClientFactory import ClientFactory
from redfish.rest.v1 import HttpClient
from redfish.rest.v1 import RestResponse
import pprint as p

iso : str = "VMware-VMvisor-Installer-7.0.0-15843807.x86_64.iso"
#iso : str = "ubuntu-20.04-live-server-amd64.iso"
response : RestResponse = None

factory : ClientFactory = ClientFactory()
client : HttpClient = factory.createConnectedClient()

p.pprint("START MANAGERS/1 #####################")
response = client.get(path="/redfish/v1/Managers/1")
p.pprint(response.dict)
p.pprint("END #####################\n")

p.pprint("START VIRTUALMEDIA #####################")
virtualMediaURI : str = response.dict["VirtualMedia"]["@odata.id"]
response = client.get(path=virtualMediaURI)
p.pprint(response.dict)
p.pprint("END #####################\n")

p.pprint("START VIRTUAL MEDIA CONFIGURATION #####################")
vmcdCfgURI : str = response.dict["Oem"]["Supermicro"]["VirtualMediaConfig"]["@odata.id"]
p.pprint("VirtualMedia - CD Configuration: "+vmcdCfgURI)
response = client.get(path=vmcdCfgURI)
vmcdCfg : dict = response.dict
p.pprint(vmcdCfg)
p.pprint("END #####################\n")


p.pprint("UPDATING VIRTUAL MEDIA CONFIGURE  #####################")
isoPath : dict = {'Host': '192.168.76.39', 'Path': '/sambashare/'+iso}
response = client.patch(path=vmcdCfgURI, body=isoPath)
p.pprint(response.dict)
p.pprint("END #####################\n")


p.pprint("START VIRTUAL MEDIA UNMOUNT #####################")
vmcdCfgActionsUnmountURI : str = vmcdCfg["Actions"]["#IsoConfig.UnMount"]["target"]
response = client.post(path=vmcdCfgActionsUnmountURI)
p.pprint(response.dict)
p.pprint("END #####################\n")


p.pprint("START VIRTUALMEDIA CD (0 Devices Attached) #####################")
response = client.get(path=virtualMediaURI)
p.pprint(response.dict)
p.pprint("END #####################\n")


p.pprint("START VIRTUAL MEDIA MOUNT#####################")
vmcdCfgActionsMountURI : str = vmcdCfg["Actions"]["#IsoConfig.Mount"]["target"]
response = client.post(path=vmcdCfgActionsMountURI)
p.pprint(response.dict)
p.pprint("END #####################\n")


p.pprint("START VIRTUALMEDIA CD (1 Device Attached) #####################")
response = client.get(path=virtualMediaURI)
vmcdURI : str = response.dict["Members"][0]["@odata.id"]
response = client.get(path=vmcdURI)
vmcd : dict = response.dict
p.pprint(vmcd)
p.pprint("END #####################\n")

factory.logoutClient(client)