import com.ibm.cloud.ngbm.redfish as rf
from com.ibm.cloud.ngbm.redfish.manage.Bios import Bios
vm : Bios = Bios()
vm.connectRedfish()
vm.updateBootOrder(rf.bootFromHdd)
vm.getBootOrder()
vm.disconnectRedfish()
