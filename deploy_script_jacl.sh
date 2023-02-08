#!/bin/sh

/opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -username wsadmin -password HUBGIWMR -lang jacl -f /tmp/websphere/jaclscript/deploy_script.jacl
