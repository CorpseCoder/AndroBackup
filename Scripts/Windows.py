import os, subprocess
from pathlib import Path
from time import sleep

comp_path = Path.cwd()
ADB_path = comp_path / "platform-tools"

def backup():
    file=open("backup.txt","r")
    data=file.readlines()
    file.close()
    for phone_path in data:
        phone_path=phone_path.strip("\n")
        try:
            command=f'cd "{ADB_path}" && adb pull "{phone_path}" "{comp_path}\\Files\\"'
            subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
            print("Backed up", phone_path)
        except subprocess.CalledProcessError as e:
            handleError(e,"Backup")
        sleep(2)
    os.system(f'cd "{ADB_path}" && adb kill-server')
    exit()

def restore():
    print("Checking for backup files")
    if os.listdir(comp_path) == []:
        print("No backups found!")
        exit()
    else:
        print("Backup found")
        file=open("backup.txt","r")
        data=file.readlines()
        file.close()
        for phone_path in data:
            phone_path=phone_path.strip("\n")
            try:
                restorees = os.listdir(f"{comp_path}\\Files")
                for i in restorees:
                    if i == phone_path.split("/")[-1] and os.path.isdir(f"Files\\{i}"):   #If it is a directory
                        for j in os.listdir(f"Files\\{i}"):
                            command=f'cd "{ADB_path}" && adb push "{comp_path}\\Files\\{i}\\{j}" "{phone_path}"'
                            subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
                    elif i == phone_path.split("/")[-1] and os.path.isfile(f"Files\\{i}"):    #If it is a file
                        command=f'cd "{ADB_path}" && adb push "{comp_path}\\Files\\{i}" "{phone_path}"'
                        subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
                    else:
                        continue
                    print("Restored", phone_path)
            except subprocess.CalledProcessError as e:
                handleError(e,"Restore")
            sleep(2)
        os.system(f'cd "{ADB_path}" && adb kill-server')
        exit()

def handleError(e,Called_Process):
    if "no devices/emulators found" in e.output:
        print("Plug your device in")
        os.system(f'cd "{ADB_path}" && adb kill-server')
        exit()
    if "This adb server's $ADB_VENDOR_KEYS is not set" in e.output:
        print("Approve USB-Debugging in your phone")
        sleep(2)
        if Called_Process == "Backup":
            backup()
        elif Called_Process == "Restore":
            restore()
    else:
        print(e.output)

if __name__ == "__main__":
    backup()
