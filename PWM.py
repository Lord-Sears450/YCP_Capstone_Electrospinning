import os
import sys
import subprocess

def initPWM():
	if os.getuid() != 0:
		os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
	else:
		subprocess.run("/home/earle-capstone/Documents/GUI/initPWM.txt", shell=True)
		

def changeDuty(duty,pin):
	cmd = "echo {} > /sys/class/pwm/pwmchip0/pwm{}/duty_cycle".format(duty,pin)
	os.system(cmd)

# ~ initPWM()
# ~ changeDuty(5000,0)
