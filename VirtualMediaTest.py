from com.ibm.cloud.ngbm.redfish.manage.VirtualMedia import VirtualMedia
iso : str = None

print("CONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
vm : VirtualMedia = VirtualMedia()
print("CONNECTED: "+str(vm.isConnectedRedfish()))
vm.connectRedfish()
print("CONNECTED: "+str(vm.isConnectedRedfish()))

print("LIST VIRTUAL MEDIA##################################")
vm.listVirtualMedia()
print("\n\n")

print("LIST VIRTUAL MEDIA DEVICE###########################")
vm.statusVirtualMediaDevice()
vm.listVirtualMediaDevice()
print("\n\n")

print("UNMOUNT VIRTUAL MEDIA DEVICE###########################")
vm.unmountVirtualMedia()
print("\n\n")

print("LIST VIRTUAL MEDIA DEVICE###########################")
vm.listVirtualMediaDevice()
print("\n\n")

print("MOUNT VIRTUAL MEDIA DEVICE###########################")
vm.mountVirtualMedia()
print("\n\n")

print("UPDATE VIRTUAL MEDIA##################################")
iso : str = "VMware-VMvisor-Installer-7.0.0-15843807.x86_64.iso"
vm.updateVirtualMediaConfig(host="192.168.76.39", path="/sambashare/"+iso)
vm.listVirtualMedia()
print("\n\n")

print("LIST VIRTUAL MEDIA DEVICE###########################")
vm.listVirtualMediaDevice()
print("\n\n")

print("UPDATE VIRTUAL MEDIA##################################")
iso : str = "ubuntu-20.04-live-server-amd64.iso"
vm.updateVirtualMediaConfig(host="192.168.76.39", path="/sambashare/"+iso)
vm.listVirtualMedia()
print("\n\n")

print("LIST VIRTUAL MEDIA DEVICE###########################")
vm.listVirtualMediaDevice()
print("\n\n")

print("DISCONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
print("CONNECTED: "+str(vm.isConnectedRedfish()))
vm.disconnectRedfish()
print("CONNECTED: "+str(vm.isConnectedRedfish()))
