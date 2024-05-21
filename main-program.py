import Linux
import Windows
import platform, subprocess, io, zipfile, requests, os

def findOS():
   print("Checking OS, please wait.")
   host=platform.system()
   if host == "Linux" or host == "Windows" or host == "Darwin":
      print("You use",host)
      checkPATH(host)
   else:
      print("I think you use an OS unknown to humanity. Is it FreeBSD? or TempleOS?")
      exit()

def checkPATH(host):
   compPath = os.path.dirname(__file__)
   if host == "Windows":
      ADBPath = compPath + "\\" + "platform-tools"
      try:
         subprocess.check_output("cd " + ADBPath + " && adb devices", shell=True, text=True)
      except:
         print("Not Installed, Please wait while it is being installed")
         r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-windows.zip",stream=True)
         z = zipfile.ZipFile(io.BytesIO(r.content))
         z.extractall(compPath)
         print("ADB Installed")
      Windows.backup(compPath, ADBPath)

   elif host == "Linux":
      ADBPath = compPath + "/" + "platform-tools/"
      try:
         subprocess.check_output("cd " + ADBPath + " && ./adb devices", shell=True, text=True)
         print("ADB is already installed")
      except:
         print("Not Installed, Please wait while it is being installed")
         r = requests.get("https://dl.google.com/android/repository/platform-tools-latest-linux.zip",stream=True)
         z = zipfile.ZipFile(io.BytesIO(r.content))
         z.extractall(compPath)
         print("ADB Installed")
      Linux.backup(compPath, ADBPath)

   else:
      print("Unsupported OS")
      exit()

findOS()
