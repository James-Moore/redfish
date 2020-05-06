from abc import ABC
from abc import abstractmethod
from redfish.rest.v1 import HttpClient
import com.ibm.cloud.ngbm.redfish as rf
from com.ibm.cloud.ngbm.redfish.factory.ClientFactory import ClientFactory
import pprint as p


class AbstractMananger(ABC):
    def __init__(self):
        self.factory: ClientFactory = ClientFactory()
        self.client: HttpClient = self.factory.createClient()
        self.connected: bool = False
        super().__init__()

    def connectRedfish(self):
        if not self.isConnectedRedfish():
            self.factory.loginClient(self.client)
            self.connected = True

    def disconnectRedfish(self):
        if self.isConnectedRedfish():
            self.factory.logoutClient(self.client)
            self.connected = False

    def isConnectedRedfish(self) -> bool:
        return self.connected
