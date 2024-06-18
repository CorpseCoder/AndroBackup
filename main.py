import Linux
import Darwin
import Windows
import platform, subprocess, io, zipfile, requests, os

def findOS():
   print("Checking OS, please wait.")
   host=platform.system()
   if host in ["Linux","Darwin","Windows"]:
      print("You use",host)
      checkPATH(host,choice)
   else:
      print("I think you use an OS unknown to humanity. Is it FreeBSD? or TempleOS?")
      exit()

def checkPATH(host,choice):
   compPath = f"{os.path.dirname(__file__)}"
   if host == "Windows":
      ADBPath = compPath + "\\platform-tools"
      try:
         subprocess.check_output(f'cd "{ADBPath}" && adb devices', shell=True, text=True)
         print("ADB is already installed")
      except:
         print("Not Installed, Please wait while it is being installed")
         r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-windows.zip",stream=True)
         z = zipfile.ZipFile(io.BytesIO(r.content))
         z.extractall(compPath)
         print("ADB Installed")
      if choice == "R":
          Windows.restore(compPath, ADBPath)
      else:
          Windows.backup(compPath, ADBPath)

   elif host == "Linux":
      ADBPath = compPath + "/platform-tools/"
      try:
          subprocess.check_output(f'cd "{ADBPath}" && ./adb devices', shell=True, text=True)
          print("ADB is already installed")
      except subprocess.CalledProcessError as e:
          if "Access denied (insufficient permissions)" in e.output:
              os.system("clear")
              print("Ignore this error")
      except:
          print("Not Installed, Please wait while it is being installed")
          r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-linux.zip",stream=True)
          z = zipfile.ZipFile(io.BytesIO(r.content))
          z.extractall(compPath)
          print("ADB Installed")
      if choice == "R":
          Linux.restore(compPath,ADBPath)
      else:
          Linux.backup(compPath,ADBPath)
   elif host == "Darwin":
      ADBPath = compPath + "/platform-tools/"
      try:
         subprocess.check_output(f'cd "{ADBPath}" && ./adb devices', shell=True, text=True)
         print("ADB is already installed")
      except:
         print("Not Installed, Please follow instruction from the README")
         r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-darwin.zip",stream=True)
         with open("platform-tools.zip","wb") as fb:
            fb.write(r.content)
         fb.close()
         os.system(f'cd "{compPath}" && unzip platform-tools.zip')
         print("ADB Installed")
      if choice == "R":
          Darwin.restore(compPath,ADBPath)
      else:
          Darwin.backup(compPath,ADBPath)
         
   else:
      print("Unsupported OS")
      exit()

print("="*50)
print("\t\tAndroBackup")
print("="*50)
print("\t\tWhat do you want to do?")
print("="*50)
print("\t\tPress B for Backup\n\t\tAnd R for Restore")
print("="*50)
choice = input("Enter your selection: ").capitalize()
if choice not in ["B","R"]:
    print("Invalid choice")
    exit()
else:
    findOS()
