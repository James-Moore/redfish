import redfish
import pprint as p
from com.ibm.cloud.ngbm.redfish.ClientFactory import ClientFactory
from redfish.rest.v1 import HttpClient

factory : ClientFactory = ClientFactory()
client : HttpClient = factory.createConnectedClient()

redfishType : dict = {"ResetType":"GracefulShutdown"}
response = client.post(path="redfish/v1/Systems/1/Actions/ComputerSystem.Reset", body=redfishType )
p.pprint(response.dict)

factory.logoutClient(client)