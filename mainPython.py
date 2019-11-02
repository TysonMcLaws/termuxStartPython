import os
from os import system, name
from colorama import Fore, Back
running = True

while running == True:
	os.system("clear")
	print(Fore.WHITE + "\nWelcome to" + Fore.GREEN +  """

   _/_/_/  _/_/_/  _/_/_/_/  _/_/_/_/  _/_/_/   _/_/_/  _/
  _/      _/  _/  _/    _/     _/     _/  _/   _/  _/  _/
 _/      _/  _/  _/    _/     _/     _/_/_/   _/  _/  _/
_/_/_/  _/_/_/  _/    _/     _/     _/   _/  _/_/_/  _/_/_/
 """)
	print(Fore.RED + "\n==========================")
	print(Fore.RED + "Please choose an option:")
	print(Fore.RED + "==========================")
	print(Fore.WHITE + "\n[01] Start Debian Linux")
	print(Fore.WHITE + "[02] Launch Lazymux")
	print(Fore.WHITE + "[03] Launch Metasploit")
	print(Fore.WHITE + "\n[00] Quit")

	control = raw_input("\nLinux Starter >>> ")

	if control == "1" or control == "01" or control == "[01]" or control == "Start Debian Linux":
		print(Fore.BLACK + Back.WHITE + "STARTING DEBIAN LINUX")
		print(Fore.WHITE + Back.BLACK + "Try to go to your VNC Server and connect to 127.0.0.1:5901")
		print("\nIf that doesn't work type \"rm -r /tmp/.X1-lock\" below. \nThen, \"/tmp/.X11-unix/X1\" \nFinally type \"vncserver-start\"\n")
		
		try:
			os.system("./start-debian.sh")
		except:
			print(Fore.WHITE + Back.BLACK + "Failure to run command.")
			print("Try launching Debian Linux manually by following these steps:")
			print("  1. Type \"./start-debian.sh\"")
	
	elif control == "2" or control == "02" or control == "[02]" or control == "Launch Lazymux":
		print(Fore.BLACK + Back.WHITE + "LAUNCHING LAZYMUX")
		print(Fore.WHITE + Back.BLACK)

		try:
			os.system("python2 Lazymux/lazymux.py")
		except:
			print(Fore.WHITE + Back.BLACK + "Failure to run command.")
			print("Try launching Lazymux manually by following these steps:")
			print("  1. Type \"cd\"")
			print("  2. Type \"cd Lazymux\"")
			print("  3. Type \"python2 lazymux.py\"")

	elif control == "0" or control == "quit" or control == "00" or control == "[00]" or control == "Quit":
		os.system("clear")
		running = False
	else:
		print("Command not recognized")

print(Fore.WHITE + Back.BLACK)
os.system("clear")
