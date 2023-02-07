import time

pathFile = '/tmp/websphere/demo.ear'
appName = 'demo-ear'
print '==============Strating Print List Application=============='
print AdminApp.list()
print '==============End List Application=============='

print '==============Uninstall the application =============='
#appStatus = AdminControl.completeObjectName('node=DefaultNode01,cell=DefaultCell01,type=Application,name=demo,*')
result = AdminControl.completeObjectName('type=Application,name=' + appName + ',*')
if (result):
  print 'Application exist and uninstalling'
  AdminApp.uninstall(appName);
else:
  print 'Application does not exist do not uninstalling'

#save
AdminConfig.save();
print '==============End uninstall application =============='

print '==============Installing application =============='
AdminApp.install(pathFile, "-appname "+ appName + " -node DefaultNode01 -server server1 -defaultbinding.virtual.host default_host -usedefaultbindings");

#save
AdminConfig.save();
print '==============Installing application done=============='

print '==============Starting application=============='
appManager = AdminControl.queryNames('cell=DefaultCell01,node=DefaultNode01,type=ApplicationManager,process=server1,*')

print appManager

AdminControl.invoke(appManager, 'startApplication', 'demo-ear')
print '==============Starting application done=============='

time.sleep(5)

print '==============Checking status application=============='
appStatus = AdminControl.completeObjectName('node=DefaultNode01,cell=DefaultCell01,type=Application,name='+appName+',*')
print appStatus

if (appStatus != ''):
  print 'The MBean for this application on cell=desapp01Cell_WAS9,node=desapp01_WAS9 is running.'
  print 'THE APPLICATION HAS BEEN STARTED'
else:
  print 'The MBean for this application on cell=desapp01Cell_WAS9,node=desapp01_WAS9 is NOT running.'
  print 'The application cannot be started on cell=desapp01Cell_WAS9,node=desapp01_WAS9.'
print '==============Checking status application done=============='
