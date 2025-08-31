import os
import subprocess
import winsound

sound_path_back = os.path.expandvars('%SystemRoot%\\Media\\Windows Background.wav')
sound_path_fore = os.path.expandvars('%SystemRoot%\\Media\\Windows Foreground.wav')
returnvalue = subprocess.call('shutdown /a', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if returnvalue == 1116:
    os.system('start /B .\MessageBox.exe 因为没有任何进行中的关机过程，所以无法中止系统关机。(1116) 错误 0 16')
    winsound.PlaySound(sound_path_fore, winsound.SND_FILENAME)
elif returnvalue == 0:
    os.system('start /B .\MessageBox.exe 计划的电源计划已被取消。(0) 成功 0 80')
    winsound.PlaySound(sound_path_back, winsound.SND_FILENAME)
else:
    os.system('start /B .\MessageBox.exe 程序遇到未知错误。(' + str(returnvalue) + ') 错误 0 16')
    winsound.PlaySound(sound_path_fore, winsound.SND_FILENAME)