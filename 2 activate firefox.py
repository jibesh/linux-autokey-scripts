# Enter script code
#window.activate("Mozilla Firefox")

retCode = window.wait_for_exist(".*Mozilla Firefox", timeOut=0)
if retCode:
    window.activate("Navigator.Firefox", matchClass = True)
else:
    system.exec_command('firefox -P "no-remote"')
    window.activate("Navigator.Firefox", matchClass = True)
    #window.activate("Mozilla Firefox")

