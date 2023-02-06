#install the application

deployWAR="/tmp/websphere/demo.war"

appName="demo"

AdminApp.install(deployWAR, "-appname "+ appName + " -node DefaultNode01 -server server1 -usedefaultbindings");

#save

AdminConfig.save();
