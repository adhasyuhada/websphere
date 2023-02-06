#Uninstall the application

deployWAR="/tmp/websphere/demo.war"

appName="demo"

AdminApp.uninstall(appName);

#save

AdminConfig.save();
