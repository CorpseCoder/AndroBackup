import os, subprocess
from time import sleep

comp_path = os.path.dirname(__file__)
ADB_path = f"{comp_path}/platform-tools/"

def checkFile(comp_path):
    try:
        file=open("backup.txt","r")
        file.close()
    except:
        file=open("backup.txt","w")
        print("Backup txt file is created, please enter the full path of the files you want to save from phone")
        while True:
            path_to_save=input("Enter a path to be backed up")
            if path_to_save.startswith("/") == False:
                path_to_save = "/storage/emulated/0/" + path_to_save
            elif path_to_save.startswith("/") == True:
                pass
            print(path_to_save,"has been added to backup list")
            choice = input("Do you want to add more? (Y/n) ")
            if choice in "Nn":
                break
        file.close()

def isEmpty(comp_path):
    try:
        if os.listdir(f"{comp_path}/Saved_Files") != []:
            return False
        elif os.listdir(f"{comp_path}/Saved_Files") == []:
            return True
    except FileNotFoundError:
        os.makedirs(f"{comp_path}/Saved_Files")

def backup(comp_path,ADB_path):
    file=open("backup.txt","r")
    data=file.readlines()
    file.close()
    isEmpty(comp_path)
    for phone_path in data:
        phone_path=phone_path.strip("\n")
        try:
            command=f'cd "{ADB_path}" && ./adb pull "{phone_path}" "{comp_path}/Saved_Files/"'
            subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
            print("Backed up", phone_path)
        except subprocess.CalledProcessError as e:
            handleError(e,"Backup")
        sleep(2)
    os.system(f'cd "{ADB_path}" && sudo ./adb kill-server')
    exit()

def restore(comp_path,ADB_path):
    print("Checking for backup files")
    if isEmpty(comp_path) == True:
        print("No backups found!")
        exit()
    elif isEmpty(comp_path) == False:
        print("Backup found")
        checkFile(comp_path)
        file=open("backup.txt","r")
        data=file.readlines()
        file.close()
        for phone_path in data:
            phone_path=phone_path.strip("\n")
            try:
                restorees = os.listdir(f"{comp_path}/Saved_Files")
                for i in restorees:
                    if phone_path.split("/")[-1] == "" and i == phone_path.split("/")[-2]:    #If it is a directory
                        command=f'cd "{ADB_path}" && ./adb push "{comp_path}/Saved_Files/{i}/" "{phone_path}"'
                    elif phone_path.split("/")[-1] != "" and i == phone_path.split("/")[-1]:    #If it is a file
                        command=f'cd "{ADB_path}" && ./adb push "{comp_path}/Saved_Files/{i}" "{phone_path}"'
                    else:
                        continue
                    subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
                    print("Restored", phone_path)
            except subprocess.CalledProcessError as e:
                handleError(e,"Restore")
            sleep(2)
        os.system(f'cd "{ADB_path}" && sudo ./adb kill-server')
        exit()

def handleError(e,Called_Process):
    if "Permission denied" in e.output:
        print("Enter sudo password to set ADB to be executable")
        os.system(f'cd "{ADB_path}" && sudo chmod +x *')
        if Called_Process == "Backup":
            backup(comp_path,ADB_path)
        elif Called_Process == "Restore":
            restore(comp_path,ADB_path)
    if "no devices/emulators found" in e.output:
        print("Plug your device in")
        os.system(f'cd "{ADB_path}" && ./adb kill-server')
        exit()
    if "Access denied (insufficient permissions)" in e.output:
        os.system(f'cd "{ADB_path}" && ./adb kill-server')
        print("Starting ADB server as sudo due to permission issue")
        os.system(f'cd "{ADB_path}" && sudo ./adb start-server')
        if Called_Process == "Backup":
            backup(comp_path,ADB_path)
        elif Called_Process == "Restore":
            restore(comp_path,ADB_path)
    if "This adb server's $ADB_VENDOR_KEYS is not set" in e.output:
        print("Approve USB-Debugging in your phone")
        sleep(2)
        if Called_Process == "Backup":
            backup(comp_path,ADB_path)
        elif Called_Process == "Restore":
            restore(comp_path,ADB_path)
    else:
        print(e.output)

if __name__ == "__main__":
    backup(comp_path,ADB_path)
