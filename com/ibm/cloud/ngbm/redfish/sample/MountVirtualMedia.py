from com.ibm.cloud.ngbm.redfish.manage.VirtualMedia import VirtualMedia
vm : VirtualMedia = VirtualMedia()
vm.connectRedfish()
vm.mountVirtualMedia()
vm.disconnectRedfish()
