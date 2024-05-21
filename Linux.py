#!/bin/python3

import os, subprocess
from time import sleep

compPath = os.path.dirname(__file__)
ADBPath = compPath + "/" + "platform-tools/"

def backup(compPath,ADBPath):
	try:
		filee=open("backup.txt","r")
	except:
		filee=open("backup.txt","w")
		print("Backup txt file is created, please enter the path of files you want to save from phone")
		filee.close()
	str=filee.readlines()
	filee.close()
	for i in str:
		i=i.rsplit("\n")
		phonePath=i[0]
		try:
			os.makedirs(compPath+"/Saved_Files")
		except FileExistsError:
			pass
		try:
			commande="cd " + ADBPath + " && ./adb pull " + phonePath + " " + compPath + "/Saved_Files/"
			subprocess.check_output(commande, shell=True, text=True, stderr=subprocess.STDOUT)
			print("Backed up", phonePath)
		except subprocess.CalledProcessError as e:
			print(e.output)
			if "Permission denied" in e.output:
				print("Enter sudo password to set ADB to be executable")
				os.system("cd " + ADBPath + " && sudo chmod +x *")

		except:
			commande="cd " + ADBPath + " && ./adb pull " + phonePath + " " + compPath + "/Saved_Files/" + " >>/dev/null"
			os.system(commande)
			print("Backed up", phonePath)
		sleep(2)
