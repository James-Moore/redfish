from com.ibm.cloud.ngbm.redfish.manage.Power import Power
client : Power = Power()
client.connectRedfish()
client.forceRestart()
client.disconnectRedfish()