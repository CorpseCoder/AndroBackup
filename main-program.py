import Linux
import Windows
import platform
from time import sleep

def findOS():
   print("Checking OS, please wait.")
   info=platform.system()
   if info == "Linux":
      print("You use Linux!")
      sleep(2)
      print("Launching app, please wait!")
      sleep(2)
      Linux.backup()
   elif info == "Darwin":
      print("You use macOS!")
      print("macOS support coming soon...")
      exit()
   elif info == "Windows":
      print("You use Windows!")
      Windows.backup()
      exit()
   else:
      print("I think you use an OS unknown to humanity. Is it FreeBSD? or TempleOS?")
      exit()

findOS()
