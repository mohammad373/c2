# c2

import os
import time
import sys
from colorama import Fore
import webbrowser as web

def __1__():
  
    os.system("clear")  
    time.sleep(2)
    print(Fore.RED + "[~] - Admin Welcime Back ;)")
    time.sleep(2)
    password = "4030"
    for i in range(5):
            try:
                    pw = inpur(Fore.RED + "\n[!] - Enter Your PassWord ==>" + Fore.BLACK + "  ")
                if pw != password:
                    print(f"\nYour Pass Word Is Not Found ;(  .  Your Have {4-i} Time More .")

                if pw == password:
                    try:
                        time.sleep(2)
                        print(Fore.GREEN + "\nOk You Are Admin ;)")
                        time.sleep(2)
                        print(Fore.GREEN + "\n[+] ~ UserName : " + Fore.RED + "mohammad373")
                        print(Fore.GREEN + "[+] ~ PassWord : "  + Fore.RED + "0990m0990")
                        time.sleep(3)
                        print(Fore.BLUE + "\nGood Bay ;)")
                        time.sleep(2)
                        sys.exit()
                    except:
                        pass
                if pw == 5:
                    try:
                        print(Fore.RED + "\n[!] - Your PassWord Is Not Found ;(  Good Bay ;)")
                        sys.exit()
                    except:
                        pass
            except:
              pass

__1__()
