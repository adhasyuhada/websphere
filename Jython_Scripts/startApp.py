appManager = AdminControl.queryNames('cell=DefaultCell01,node=DefaultNode01,type=ApplicationManager,process=server1,*')

print appManager

AdminControl.invoke(appManager, 'startApplication', 'demo-ear')


