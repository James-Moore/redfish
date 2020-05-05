import redfish
import pprint as p
from com.ibm.cloud.ngbm.redfish.ClientFactory import ClientFactory
from redfish.rest.v1 import HttpClient

factory : ClientFactory = ClientFactory()
client : HttpClient = factory.createConnectedClient()

response = client.get(path="/redfish/v1/Systems/1/" )
p.pprint("System Power is " + response.dict["PowerState"])

factory.logoutClient(client)
