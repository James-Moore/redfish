from com.ibm.cloud.ngbm.redfish.manage.VirtualMedia import VirtualMedia
iso : str = None

print("CONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
vm : VirtualMedia = VirtualMedia()
print("CONNECTED: "+str(vm.isConnectedRedfish()))
vm.connectRedfish()
print("CONNECTED: "+str(vm.isConnectedRedfish()))

print("UNMOUNT VIRTUAL MEDIA DEVICE###########################")
vm.unmountVirtualMedia()
print("\n\n")

print("UPDATE VIRTUAL MEDIA##################################")
vm.updateVirtualMediaConfig(host="192.168.76.27", path="/sambashare/ubuntu-18.04.4-live-server-amd64.iso")
#vm.updateVirtualMediaConfig(host="192.168.76.27", path="/sambashare/mini.iso")
vm.mountVirtualMedia()

print("LIST VIRTUAL MEDIA DEVICE###########################")
vm.listVirtualMediaDevice()
print("\n\n")

print("DISCONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
print("CONNECTED: "+str(vm.isConnectedRedfish()))
vm.disconnectRedfish()
print("CONNECTED: "+str(vm.isConnectedRedfish()))
