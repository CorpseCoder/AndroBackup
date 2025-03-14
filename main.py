import Linux, Darwin, Windows
import platform, subprocess, io, zipfile, os
from time import sleep

def installModules():
    try:
        import requests
    except ModuleNotFoundError:
        os.system("python3 -m pip install requests")

def findOS():
   print("Checking OS, please wait.")
   host_name=platform.system()
   return host_name

def checkPATH(host):
   import requests
   comp_path = f"{os.path.dirname(__file__)}"
   if host == "Windows":
      ADB_path = comp_path + "\\platform-tools"
      try:
         subprocess.check_output(f'cd "{ADB_path}" && adb devices', shell=True, text=True)
         print("ADB is already installed")
      except:
         print("Not Installed, Please wait while it is being installed")
         r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-windows.zip",stream=True)
         z = zipfile.ZipFile(io.BytesIO(r.content))
         z.extractall(compPath)
         print("ADB Installed")
      return comp_path,ADB_path

   elif host == "Linux":
      ADB_path = comp_path + "/platform-tools/"
      try:
          subprocess.check_output(f'cd "{ADB_path}" && ./adb devices', shell=True, text=True)
          print("ADB is already installed")
      except subprocess.CalledProcessError as e:
          if "Access denied (insufficient permissions)" in e.output:
              os.system("clear")
              print("ADB Installed")
      except:
          print("Not Installed, Please wait while it is being installed")
          r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-linux.zip",stream=True)
          z = zipfile.ZipFile(io.BytesIO(r.content))
          z.extractall(compPath)
          print("ADB Installed")
      return comp_path, ADB_path

   elif host == "Darwin":
      ADB_path = comp_path + "/platform-tools/"
      try:
         subprocess.check_output(f'cd "{ADB_path}" && ./adb devices', shell=True, text=True)
         print("ADB is already installed")
      except:
         print("Not Installed, Please wait while it is being installed")
         r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-darwin.zip",stream=True)
         with open("platform-tools.zip","wb") as fb:
            fb.write(r.content)
         fb.close()
         os.system(f'cd "{comp_path}" && unzip platform-tools.zip')
         print("ADB Installed")
      return comp_path,ADB_path
         
   else:
      print("Unsupported OS")
      exit()

def mainMenu(host):
    installModules()

    print("Checking system specifications")
    sleep(5)

    if host in ["Linux","Darwin","Windows"]:
        print("Host runs",host)
    else:
        print("Unrecognized host!")
        exit()

    print("\v"*100)

    print("Checking whether ADB is installed")

    comp_path,ADB_path = checkPATH(host)

    print("\v"*100)

    print("="*50)
    print("\t\tAndroBackup")
    print("="*50)
    print("\t\tWhat do you want to do?")
    print("="*50)
    print("\t\tPress B for Backup\n\t\tAnd R for Restore")    #Rework needed
    print("="*50)
    choice = input("Enter your selection: ").capitalize()

    if choice == "B":
        if host == "Windows":
            Windows.backup(comp_path,ADB_path)
        elif host == "Darwin":
            Darwin.backup(comp_path,ADB_path)
        elif host == "Linux":
            Linux.backup(comp_path,ADB_path)
        else:
            print("Unknown host!")

    elif choice == "R":
        if host == "Windows":
            Windows.restore(comp_path,ADB_path)
        elif host == "Darwin":
            Darwin.restore(comp_path,ADB_path)
        elif host == "Linux":
            Linux.restore(comp_path,ADB_path)
        else:
            print("Unknown host!")

    elif choice not in ["B","R"]:
        print("Invalid choice")
        exit()

mainMenu(findOS())
