import os

returnvalue = os.system('shutdown /a')
if returnvalue == 1116:
    os.system('start C:\\AutoShutdownPlanner\\NoPlan.vbs')
elif returnvalue == 0:
    os.system('start C:\\AutoShutdownPlanner\\Success.vbs')
else:
    os.system('start C:\\AutoShutdownPlanner\\Failed.vbs')