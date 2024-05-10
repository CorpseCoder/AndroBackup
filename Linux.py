#!/bin/python3

import os, subprocess
from time import sleep

def backup():
	filee=open("backup.txt","r")
	str=filee.readlines()
	for i in str:
		i=i.rsplit("\n")
		path=i[0]
		try:
			os.makedirs("~/Downloads/Saved_Files")
		except FileExistsError:
			pass
		if exists_ == True:
			commande="adb pull " + path + " ~/Downloads/Saved_Files/ >> /dev/null"			
		else:
			commande="cd platform-tools/ && adb pull " + path + " ~/Downloads/Saved_Files/ >> /dev/null"
		os.system(commande)
		print("Backed up",path)
		sleep(2)

def checkPATH():
	print("Checking whether ADB is in PATH")
	try:
		subprocess.check_output("adb devices", shell=True, text=True)
	except:
		print("Not Installed")
		exists_ = False
		backup()
	else:
		print("ADB is installed!")
		exists_ = True
		backup()
