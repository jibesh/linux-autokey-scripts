nowtime = system.exec_command('date +"%Y-%m-%d-%H%M-%S"', getOutput=True)
keyboard.send_keys(str(nowtime))
