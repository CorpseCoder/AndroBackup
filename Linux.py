#!/bin/python3

import os, subprocess
from time import sleep

def backup():
	filee=open("backup.txt","r")
	str=filee.readlines()
	for i in str:
		i=i.rsplit("\n")
		path=i[0]
		commande="cd platform-tools/ && adb pull " + path + " ~/Downloads/Success/ >> /dev/null"
		os.system(commande)
		print("Backed up",path)
		sleep(2)

# def checkPATH():
# 	print("Checking whether ADB is in PATH")
# 	try:
# 		subprocess.check_output("adb devices", shell=True, text=True)
# 	except:
# 		print("Not Installed")
# 		sleep(2)
# 		exit()
# 	else:
# 		print("ADB is installed!")
# 		backup()
