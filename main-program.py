import Linux
import Windows
import platform

def findOS():
   print("Checking OS, please wait.")
   info=platform.system()
   if info == "Linux":
      print("You use Linux!")
      Linux.checkPATH()
   elif info == "Darwin":
      print("You use macOS!")
      print("macOS support coming soon...")
      exit()
   elif info == "Windows":
      print("You use Windows!")
      Windows.backup()
   else:
      print("I think you use an OS unknown to humanity. Is it FreeBSD? or TempleOS?")
      exit()

findOS()
