from com.ibm.cloud.ngbm.redfish.manage.VirtualMedia import VirtualMedia
isoName : str = None

print("CONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
vm : VirtualMedia = VirtualMedia()
print("CONNECTED: "+str(vm.isConnectedRedfish()))
vm.connectRedfish()
print("CONNECTED: "+str(vm.isConnectedRedfish()))

#print("UNMOUNT VIRTUAL MEDIA DEVICE###########################")
#vm.unmountVirtualMedia()

print("LIST VIRTUAL MEDIA##################################")
vm.listVirtualMedia()
print("\n\n")

print("LIST VIRTUAL MEDIA DEVICE###########################")
vm.statusVirtualMediaDevice()
vm.listVirtualMediaDevice()
print("\n\n")

print("UPDATE VIRTUAL MEDIA##################################")

isoHost: str = "https://192.168.76.27"
isoPath: str = "/iso/"
isoName : str = "mini.iso"

#isoHost: str = "192.168.76.27"
#isoPath: str = "/sambashare/"
#isoName : str = "mini.iso"

print("CONFIG UPDATE: ")
print("ISO_HOST: "+isoHost)
print("ISO_PATH: "+isoPath)
print("ISO_NAME: "+isoName)
vm.updateVirtualMediaConfig(host=isoHost, path=isoPath + isoName)
print("\n\n")

print("MOUNT VIRTUAL MEDIA DEVICE###########################")
vm.mountVirtualMedia()
print("\n\n")

print("LIST VIRTUAL MEDIA##################################")
vm.listVirtualMedia()
print("\n\n")

print("LIST VIRTUAL MEDIA DEVICE###########################")
vm.listVirtualMediaDevice()
print("\n\n")

print("DISCONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
print("CONNECTED: "+str(vm.isConnectedRedfish()))
vm.disconnectRedfish()
print("CONNECTED: "+str(vm.isConnectedRedfish()))
