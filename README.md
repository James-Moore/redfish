# redfish
### Distributed Management Task Force

https://www.dmtf.org/standards/redfish

The Distributed Management Task Force has created a server management standard called Redfish. 
DMTF’s Redfish® is a standard designed to deliver simple and secure management for converged, 
hybrid IT and the Software Defined Data Center (SDDC). Both human readable and machine capable, 
Redfish leverages common Internet and web services standards to expose information directly to 
the modern tool chain.

The DMTF's Python Library can be found here:
https://github.com/DMTF/python-redfish-library

### Environment

#### Python

Requires the installation of Python 3

Install required python libraries using requirements.txt

#### Forward Redfish Port

In order to interact with your server's BMC you'll likely need to port forward.  The server's ip 
address is the same as the IPMI ip.  Use ForwardRedfishPort.sh to easily port forward using ssh.
An example usage is bellow:

```
$ export REDFISH_HOME=~/PycharmProjects/redfish/
$ echo $REDFISH_HOME 
/Users/james.mooreibm.com/PycharmProjects/redfish/
$ source bin/forwardRedfishPort
$ source bin/forwardRedfishPort 
$ redfishEnable 8443 xxx.xxx.xxx.xxx 443 jump-server
Authorized uses only. All activity may be monitored and reported.
$ ps -ef | grep ssh
  ...
  501 47579     1   0 11:50AM ??         0:00.00 ssh -fqTnN -L 0.0.0.0:8443:xxx.xxx.xxx.xxx:443 jump-server
  501 47578     1   0 11:50AM ttys000    0:00.09 ssh -W [10.200.143.39]:22 dal-jump
  ...
$ curl -k https://localhost:8443/redfish/v1/ | jq -r .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   863  100   863    0     0   1143      0 --:--:-- --:--:-- --:--:--  1141
{
  "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
  "@odata.type": "#ServiceRoot.v1_1_0.ServiceRoot",
  "@odata.id": "/redfish/v1/",
  "Id": "RootService",
  "Name": "Root Service",
  "RedfishVersion": "1.0.1",
  "UUID": "00000000-0000-0000-0000-AC1F6BFA9700",
  "Systems": {
    "@odata.id": "/redfish/v1/Systems"
  },
  "Chassis": {
    "@odata.id": "/redfish/v1/Chassis"
  },
  "Managers": {
    "@odata.id": "/redfish/v1/Managers"
  },
  "Tasks": {
    "@odata.id": "/redfish/v1/TaskService"
  },
  "SessionService": {
    "@odata.id": "/redfish/v1/SessionService"
  },
  "AccountService": {
    "@odata.id": "/redfish/v1/AccountService"
  },
  "EventService": {
    "@odata.id": "/redfish/v1/EventService"
  },
  "UpdateService": {
    "@odata.id": "/redfish/v1/UpdateService"
  },
  "Registries": {
    "@odata.id": "/redfish/v1/Registries"
  },
  "JsonSchemas": {
    "@odata.id": "/redfish/v1/JsonSchemas"
  },
  "Links": {
    "Sessions": {
      "@odata.id": "/redfish/v1/SessionService/Sessions"
    }
  },
  "Oem": {}
}
```
  