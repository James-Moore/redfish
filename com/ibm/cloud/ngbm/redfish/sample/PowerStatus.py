from com.ibm.cloud.ngbm.redfish.manage.Power import Power
client : Power = Power()
client.connectRedfish()
print("Power On: "+str(client.isPowerOn()))
client.disconnectRedfish()