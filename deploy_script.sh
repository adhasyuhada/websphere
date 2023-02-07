#!/bin/sh

/opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -username wsadmin -password HUBGIWMR -lang jython -f /opt/IBM/WebSphere/AppServer/Jython_Scripts/listApplications.py

/opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -username wsadmin -password HUBGIWMR -lang jython -f /opt/IBM/WebSphere/AppServer/Jython_Scripts/uninstallApp.py

/opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -username wsadmin -password HUBGIWMR -lang jython -f /opt/IBM/WebSphere/AppServer/Jython_Scripts/installApp.py

/opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -username wsadmin -password HUBGIWMR -lang jython -f /opt/IBM/WebSphere/AppServer/Jython_Scripts/statusApp.py
