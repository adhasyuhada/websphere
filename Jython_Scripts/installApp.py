#install the application

deployEAR="/tmp/websphere/demo.ear"

appName="demo-ear"

AdminApp.install(deployEAR, "-appname "+ appName + " -node DefaultNode01 -server server1 -defaultbinding.virtual.host default_host -usedefaultbindings");

#save

AdminConfig.save();
