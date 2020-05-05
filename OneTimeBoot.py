import redfish
import pprint as p

redfishConnect = redfish.redfish_client(base_url="https://airboat1.fyre.ibm.com:8443", username="root", password="ibm-Genesis-Cl0ud", default_prefix="/redfish/v1")
redfishConnect.login(username="root", password="ibm-Genesis-Cl0ud", auth="session")
sessionKey = redfishConnect.get_session_key()
print("Session Key: "+sessionKey)
response = redfishConnect.get(path="/redfish/v1/Systems/1/" )
p.pprint(response.dict)
redfishConnect.logout()