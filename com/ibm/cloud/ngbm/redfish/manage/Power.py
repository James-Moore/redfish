import pprint as p
import com.ibm.cloud.ngbm.redfish as rf
from com.ibm.cloud.ngbm.redfish.manage.AbstractManager import AbstractMananger

class Power(AbstractMananger):
  def __init__(self):
      super().__init__()

  def isPowerOn(self) -> bool:
    if not self.isConnectedRedfish():
        p.pprint("Virtual Media client not connected.  Connect and try again.")
        return

    response = self.client.get(path=rf.systems)
    return response.dict["PowerState"] == rf.powerStatusOn

  def startup(self, startupType: dict):
      if not self.isConnectedRedfish():
          return

      if self.isPowerOn():
         return

      response = self.client.post(path=rf.resetActionURI, body=startupType)
      p.pprint(response.dict)

  def shutdown(self, shutdownType: dict):
      if not self.isConnectedRedfish():
          return

      if not self.isPowerOn():
         return

      response = self.client.post(path=rf.resetActionURI, body=shutdownType)
      p.pprint(response.dict)

  def powerOn(self):
      self.startup(startupType=rf.resetActionOn)

  def powerOff(self):
      self.shutdown(shutdownType=rf.resetActionOff)

  def forcePowerOn(self):
      self.startup(startupType=rf.resetActionForceOn)

  def forcePowerOff(self):
      self.shutdown(shutdownType=rf.resetActionForceOff)