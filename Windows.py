import os, subprocess
from time import sleep

compPath = os.path.dirname(__file__)
ADBPath = f"{compPath}\\platform-tools\\"

def backup(compPath,ADBPath):
    try:
        file=open("backup.txt","r")
    except:
        file=open("backup.txt","w")
        print("Backup txt file is created, please enter the path of files you want to save from phone")
    str=file.readlines()
    file.close()
    for i in str:
        i=i.rsplit("\n")
        phonePath=i[0]
        try:
            os.makedirs(f"{compPath}\\Saved_Files")
        except FileExistsError:
            pass

        try:
            command=f'cd "{ADBPath}" && adb pull {phonePath} "{compPath}"\\Saved_Files\\'
            subprocess.check_output(command, shell=True, text=True)
            print("Backed up",phonePath)
        except subprocess.CalledProcessError as e:
            if "no devices/emulators found" in e.output:
                print("Plug your phone in")
                os.system(f"cd {ADBPath} && adb kill-server")
                exit()
            if "This adb server's $ADB_VENDOR_KEYS is not set" in e.output:
                print("Approve USB-Debugging in your phone")
                sleep(2)
                backup(compPath,ADBPath)
            else:
                print(e.output)
        sleep(2)
    os.system(f"cd {ADBPath} && adb kill-server")
    exit()
