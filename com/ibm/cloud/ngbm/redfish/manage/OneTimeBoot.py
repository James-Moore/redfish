import pprint as p
from com.ibm.cloud.ngbm.redfish.factory.ClientFactory import ClientFactory
from redfish.rest.v1 import HttpClient

factory : ClientFactory = ClientFactory()
client : HttpClient = factory.createConnectedClient()

#TODO implement one time boot example
response = client.get(path="/redfish/v1/Systems/1/" )
p.pprint(response.dict)


factory.logoutClient(client)
