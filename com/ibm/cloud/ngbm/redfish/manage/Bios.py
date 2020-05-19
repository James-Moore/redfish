import pprint as p
import com.ibm.cloud.ngbm.redfish as rf
from com.ibm.cloud.ngbm.redfish.manage.AbstractManager import AbstractMananger
from redfish.rest.v1 import RestResponse

class Bios(AbstractMananger):
  def __init__(self):
      super().__init__()

  def updateBootOrder(self, bootSourceOverrideTarget : str):
      if not self.isConnectedRedfish():
          p.pprint("Bios client is not connected.  Connect and try again.")
          return

      bootUpdate : dict = {
          "Boot": {
              "BootSourceOverrideEnabled": "Once",
              'BootSourceOverrideMode': 'UEFI',
              "BootSourceOverrideTarget": bootSourceOverrideTarget
          }
      }

      response: RestResponse = self.client.patch(path=rf.systems, body=bootUpdate)
      p.pprint(response.dict)

  def getBootOrder(self):
      if not self.isConnectedRedfish():
          p.pprint("Bios client is not connected.  Connect and try again.")
          return

      response: RestResponse = self.client.get(path=rf.systems)
      p.pprint(response.dict)
