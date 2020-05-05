from com.ibm.cloud.ngbm.redfish.manage.Power import Power
client : Power = Power()
client.connectRedfish()
client.powerOff()
client.disconnectRedfish()