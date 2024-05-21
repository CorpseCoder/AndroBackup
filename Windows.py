import os
from time import sleep

compPath = os.path.dirname(__file__)
ADBPath = compPath + "\\" + "platform-tools\\"

def backup(compPath,ADBPath):
	try:
		filee=open("backup.txt","r")
	except:
		filee=open("backup.txt","w")
		print("Backup txt file is created, please enter the path of files you want to save from phone")
	str=filee.readlines()
	filee.close()
	for i in str:
		i=i.rsplit("\n")
		phonePath=i[0]
		try:
			os.makedirs(compPath+"\\Saved_Files")
		except FileExistsError:
			pass

		commande="cd " + ADBPath + " && adb pull " + phonePath + " " + compPath + "\\Saved_Files\\"
		os.system(commande)
		print("Backed up",phonePath)
		sleep(2)
