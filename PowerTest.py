from com.ibm.cloud.ngbm.redfish.manage.Power import Power

print("CONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
client : Power = Power()
client.connectRedfish()
print("CONNECTED: "+str(client.isConnectedRedfish()))

print("POWER STATUS##################################")
print("Power On: "+str(client.isPowerOn()))
print("\n\n")

print("POWER ON##################################")
client.powerOn()
print("Power On: "+str(client.isPowerOn()))
print("\n\n")

print("POWER OFF##################################")
client.forcePowerOff()
print("Power On: "+str(client.isPowerOn()))
print("\n\n")

client.disconnectRedfish()
