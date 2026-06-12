from Scripts import Linux, Windows
import platform, subprocess, os
from time import sleep

def checkPATH(host):
    import requests
    from pathlib import Path
    if host in ["windows","darwin","linux"]:
        ADB_path = Path(".") / "platform-tools"
        try:
            if host == "windows":
                subprocess.check_output(f'cd "{ADB_path}" && adb devices', shell=True, text=True)
            elif host in ["darwin","linux"]:
                subprocess.check_output(f'cd "{ADB_path}" && ./adb devices', shell=True, text=True)
            print("ADB is already installed")
        except:
            print("Not Installed, Please wait while it is being installed")
            r = requests.get(f"https://dl.google.com/android/repository/platform-tools-latest-{host}.zip",stream=True)
            with open("platform-tools.zip","wb") as f:
                f.write(r.content)
            if host == "windows":
                os.system(f'cd "{Path(".")}" && tar -xf platform-tools.zip')
            elif host in ["darwin","linux"]:
                os.system(f'cd "{Path(".")}" && unzip platform-tools.zip')

            os.remove("platform-tools.zip")
            print("ADB Installed")

def mainMenu():
    print("Checking system specifications")
    sleep(5)
    
    host = platform.system()

    if host in ["Linux","Darwin","Windows"]:
        print("Host runs",host)
    else:
        print("Unrecognized host!")
        exit()

    print("\v"*100)

    print("Checking whether ADB is installed")
    checkPATH(host.lower())

    print("\v"*100)

    print("="*50)
    print("\t\tAndroBackup")
    print("="*50)
    print("\t\tWhat do you want to do?")
    print("="*50)
    print("\t\tEnter B for Backup\n\t\tAnd R for Restore")    #Rework needed
    print("="*50)
    choice = input("Enter your selection: ").lower()

    if choice in "backup":
        if host == "Windows":
            Windows.backup()
        elif host in ["Darwin","Linux"]:
            Linux.backup()

    elif choice in "restore":
        if host == "Windows":
            Windows.restore()
        elif host in ["Darwin","Linux"]:
            Linux.restore()

    else:
        print("Invalid choice")
        exit()

mainMenu()
