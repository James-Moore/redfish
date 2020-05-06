import pprint as p
import com.ibm.cloud.ngbm.redfish as rf
from com.ibm.cloud.ngbm.redfish.manage.AbstractManager import AbstractMananger
from redfish.rest.v1 import RestResponse

class VirtualMedia(AbstractMananger):
  def __init__(self):
      super().__init__()

  def getVirtualMedia(self) -> dict:
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      response: RestResponse =self.client.get(path=rf.managers)
      uri: str = response.dict[rf.virtualMediaKey][rf.odataIdKey]
      response =self.client.get(path=uri)
      virtualMedia: dict = response.dict

      return virtualMedia

  def listVirtualMedia(self):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      virtualMedia: dict = self.getVirtualMedia()
      p.pprint(virtualMedia)

  def statusVirtualMediaDevice(self):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      virtualMedia: dict = self.getVirtualMedia()
      count : int = virtualMedia[rf.virtualMediaMembersCountKey]
      p.pprint("Virtual Media Devices Mounted: "+str(count))

  def isAttachedVirtualMediaDevice(self):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      virtualMedia: dict = self.getVirtualMedia()
      count: int = virtualMedia[rf.virtualMediaMembersCountKey]
      return count != 0

  def listVirtualMediaDevice(self):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      if not self.isAttachedVirtualMediaDevice():
          p.pprint("Can not list virtual media devices because none are attached.")
          return

      response: RestResponse =self.client.get(path=rf.managers)
      virtualMediaURI: str = response.dict[rf.virtualMediaKey][rf.odataIdKey]

      response =self.client.get(path=virtualMediaURI)
      vmcdURI: str = response.dict[rf.virtualMediaMembersKey][0][rf.odataIdKey]

      response =self.client.get(path=vmcdURI)
      p.pprint(response.dict)

  def updateVirtualMediaConfig(self, host : str, path : str):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      iso: dict = {rf.hostKey: host, rf.pathKey: path}

      response : RestResponse =self.client.get(path=rf.managers)
      virtualMediaURI: str = response.dict[rf.virtualMediaKey][rf.odataIdKey]

      response =self.client.get(path=virtualMediaURI)
      vmcdCfgURI: str = response.dict[rf.oemKey][rf.supermicroKey][rf.virtualMediaConfigKey][rf.odataIdKey]

      response =self.client.patch(path=vmcdCfgURI, body=iso)
      p.pprint(response.dict)

  def actionVirtualMedia(self, virtualMediaAction: str):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      response: RestResponse =self.client.get(path=rf.managers)
      virtualMediaURI: str = response.dict[rf.virtualMediaKey][rf.odataIdKey]

      response =self.client.get(path=virtualMediaURI)
      vmcdCfgURI: str = response.dict[rf.oemKey][rf.supermicroKey][rf.virtualMediaConfigKey][rf.odataIdKey]

      response =self.client.get(path=vmcdCfgURI)
      vmcdCfgActionsUnmountURI: str = response.dict[rf.actionsKey][virtualMediaAction][rf.virtualMediaTargetKey]

      response =self.client.post(path=vmcdCfgActionsUnmountURI)
      p.pprint(response.dict)

  def mountVirtualMedia(self):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      self.actionVirtualMedia(virtualMediaAction=rf.virtualMediaMountKey)

  def unmountVirtualMedia(self):
      if not self.isConnectedRedfish():
          p.pprint("Virtual Media client not connected.  Connect and try again.")
          return

      self.actionVirtualMedia(virtualMediaAction=rf.virtualMediaUnmountKey)