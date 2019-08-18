import os
from time import *
from datetime import datetime

print ("\033[1;35m ")
os.system("figlet Hello Guys")

name = input("\033[1;36mEnter Your Name Please ===》\033[1;32m")


print ("[                    ] 0% ")
sleep(3)
print ("\033[1;31m ")
print ("[=====               ] 25%")
sleep(3)
print ("\033[1;35m ")
print ("[==========          ] 50%")
sleep(3)
print ("\033[1;33 ")
print ("[===============     ] 75%")
sleep(3)
print ("\033[1;37m ")
print ("[====================] 100%\033[1;31m")
sleep(3)


os.system("cowsay my name is " + name + " i am a Donkey")
sleep(6)
os.system("figlet dont angry")
os.system("figlet just joke Bro")
