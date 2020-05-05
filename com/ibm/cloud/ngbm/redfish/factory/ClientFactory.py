import redfish
from redfish.rest.v1 import HttpClient
import pprint as p
import com.ibm.cloud.ngbm.redfish as rf

class ClientFactory:
  def __init__(self):
    pass

  def createClient(self) -> HttpClient:
    return redfish.redfish_client(base_url=rf.target, username=rf.username, password=rf.password,
                                  default_prefix=rf.defaultPrefix)
  def createConnectedClient(self) -> HttpClient:
    client = self.createClient()
    self.loginClient(client)
    return client

  def printSessionKey(self, client : HttpClient):
    p.pprint("Session Key: "+client.get_session_key())

  def loginClient(self, client : HttpClient):
    client.login(username=rf.username, password=rf.password, auth=rf.authentication)

  def logoutClient(self, client : HttpClient):
    client.logout()
