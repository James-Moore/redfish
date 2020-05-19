import pprint as p
import com.ibm.cloud.ngbm.redfish as rf
from com.ibm.cloud.ngbm.redfish.manage.AbstractManager import AbstractMananger
from redfish.rest.v1 import RestResponse

class Console(AbstractMananger):
  def __init__(self):
      super().__init__()

  def getConsoleURI(self) -> str:
      if not self.isConnectedRedfish():
          p.pprint("Console client not connected.  Connect and try again.")
          return

      response: RestResponse =self.client.get(path=rf.managers)
      uri: str = response.dict[rf.oemKey][rf.supermicroKey][rf.consoleKey][rf.odataIdKey]

      response =self.client.get(path=uri)
      console: dict = response.dict

      return console[rf.uriKey]

  def getConsole(self):
      uri : str = self.getConsoleURI()
      p.pprint(uri)
