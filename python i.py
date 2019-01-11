# opens the current Sublime Text file in Python3 -i

import re
winTitle = window.get_active_title()
maybematch = re.match(".*?\.py - Sublime Text", winTitle)

if type(maybematch) == type(None): 
    pass
else:
    fulldir = winTitle.split(" - Sublime Text")[0]
    filename = fulldir.split("/")[-1]
    directory = "/".join(fulldir.split("/")[:-1]) 
    directory = re.sub("^~/", "", directory)
    #dialog.info_dialog("hi", directory)
    cmdstring = "gnome-terminal --working-directory=\""+directory+"\" --command \"python3 -i "+filename+"\" --title \""+filename+"\" &"
    #dialog.info_dialog("hi", cmdstring)
    system.exec_command(cmdstring)

# win + d to exit. weird.
# dir() shows current stuff