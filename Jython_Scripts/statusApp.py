appStatus = AdminControl.completeObjectName('node=DefaultNode01,cell=DefaultCell01,type=Application,name=demo-ear,*')
print appStatus

if (appStatus != ''):
  print 'The MBean for this application on cell=desapp01Cell_WAS9,node=desapp01_WAS9 is running.'
  print 'THE APPLICATION HAS BEEN STARTED'
else:
  print 'The MBean for this application on cell=desapp01Cell_WAS9,node=desapp01_WAS9 is NOT running.'
  print 'The application cannot be started on cell=desapp01Cell_WAS9,node=desapp01_WAS9.'




