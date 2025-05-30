from platform import system
import sys
import os
import datetime   
from time import sleep
import facebook
import time
import datetime
from platform import system
import sys
import os
import datetime   
from time import sleep
import time
from datetime import datetime

def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
    try:
        models = ['requests', 'colorama']
        for model in models:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
                else:
                    os.system('python -m pip install {}'.format(model))
                print(' ')
                print('[+] {} has been installed successfully, Restart the program.'.format(model))
                sys.exit()
                print(' ')
            except:
                print('[-] Install {} manually.'.format(model))
                print(' ')
    except:
        pass


import base64
import json
import time
import sys
import os
import re
import binascii
import time
import json
import random
import threading
import pprint
import smtplib
import telnetlib
import os.path
import hashlib
import string
import glob
import sqlite3
import urllib
import argparse
import marshal
import datetime   
from platform import system
from datetime import datetime
import facebook
import time
import datetime
from platform import system
import sys
import os
import datetime   
from time import sleep
import time
from datetime import datetime

try:
    import requests
    from colorama import Fore
    from colorama import init
except:
    modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
    if system() == 'Linux':
        os.system('clear')
    else:
        if system() == 'Windows':
            os.system('cls')


cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[1;37;1m'  # mode 31 = red foreground
RESET = '\033[1;37;1m'  # mode 0  = reset
BLUE = "\033[1;37;1m"
WHITE = "\033[1;37;1m",
YELLOW = "\033[1;37;1m",
CYAN = "\033[1;37;1m"
MAGENTA = "\033[1;37;1m",
GREEN = "\033[1;37;1m"
RESET = "\033[1;37;1m"
BOLD = '\033[1;37;1m'
REVERSE = "\033[1;37;1m"

def logo():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    x = """
   


$$\    $$\                                             
$$ |   $$ |                                            
$$ |   $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\  
\$$\  $$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\ 
 \$$\$$  / $$$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ |
  \$$$  /  $$   ____|$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |
   \$  /   \$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |
    \_/     \_______|\__|  \__| \______/ \__| \__| \__|
                                                                                                                                                                  

$$$$$$$\            $$\                     
$$  __$$\           $$ |                    
$$ |  $$ |$$\   $$\ $$ | $$$$$$\  $$\   $$\ 
$$$$$$$  |$$ |  $$ |$$ |$$  __$$\ \$$\ $$  |
$$  __$$< $$ |  $$ |$$ |$$$$$$$$ | \$$$$  / 
$$ |  $$ |$$ |  $$ |$$ |$$   ____| $$  $$<  
$$ |  $$ |\$$$$$$  |$$ |\$$$$$$$\ $$  /\$$\ 
\__|  \__| \______/ \__| \_______|\__/  \__|                                                                                                 
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
logo()
testPY()
print('''\033[1;33m---------------------------------------------------------------------\n''')
def venom():
    clear = "\x1b[0m"
    colors = [35, 33, 36]

    y = '''
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mN4M3    \033[1;91m: \033[1;96mH4RSH SINGH R4JPUT \033[1;97m                              ║
\033[1;97m║\033[1;93m* \033[1;97mRULL3X  \033[1;91m: \033[1;96mV3N0M W4NT3D RULL3X  \033[1;97m                            ║
\033[1;97m║\033[1;93m* \033[1;97m0WN3R   \033[1;91m: \033[1;96mSIIDDH4RTH R4J  \033[1;97m                                 ║
\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;96mhttps://www.facebook.com/your.dad.harsh\033[1;97m          ║
\033[1;97m║\033[1;93m* \033[1;97mM3MB3R 1\033[1;91m: \033[1;96m4SHU \033[1;97m                                            ║
\033[1;97m║\033[1;93m*\033[1;97m M3MB3R 2\033[1;91m:\033[1;96m 44RIIZ \033[1;97m                                          ║
\033[1;97m║\033[1;93m* \033[1;97mM3MB3R 3\033[1;91m: \033[1;96mRUDR4                                            \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mM3MB3R 4\033[1;91m: \033[1;96mM4X                                              \033[1;97m║
\033[1;97m║\033[1;93m* \033[1;97mM3MB3R 5\033[1;91m: \033[1;96mS4IY4N                     \033[1;97m                      ║
\033[1;97m╚═════════════════════════════════════════════════════════════╝

'''
    for N, line in enumerate(y.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
    	
venom()

print('''\033[1;36m---------------------------------------------------------------------\n''')
print('''\033[1;35m-=[ Facebook Tool Pool Ka Super Hero Venom Wanted Rullex ]=-''')
print('''\033[1;33m-=[ Contact Us :: https://www.facebook.com/your.dad.harsh/]=-\n''')
print('''\033[1;36m---------------------------------------------------------------------\n''')
i = datetime.now()
print(i.strftime("\033[1;32m[#] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
print('''\033[1;32m[#] _ Tool Fucker == > [ Harsh Rajput ]\n''')

print("\033[1;36;40m", end="")

token_file = input("[+] Enter The File Path For Tokens :: ")

def get_profile_name(access_token):
    graph = facebook.GraphAPI(access_token=access_token, version='2.8')
    user_info = graph.get_object('me')
    profile_name = user_info['name']
    return profile_name
    

with open(token_file, 'r') as f2:
	access_tokens = f2.read().splitlines()

for index, access_token in enumerate(access_tokens, 1):
	profile_name = get_profile_name(access_token)
	print(f"{index}. All Profile Name : {profile_name}")


print("\033[1;32;40m", end = "")
def post_comment(graph, post_link, message):
    try:
        graph.put_object(parent_object='100006813250942_' + post_link, connection_name='comments', message=message)        
        print("\033[1;32;40m", end = "")       
        e =datetime.now()       
        print("\033[1;32;40m", end = "")
        print (e.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))        
        print(f"--> Message Successfully Sent By Aw'shu :D ::-->> {message}\n")
    except Exception as e:
        print("\033[1;31;40m", end = "")
        o =datetime.now()
        print (o.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
        print(f"--> Error occurred while posting comment : {e}\n")
        time.sleep(30)

print("\033[1;36;40m", end="")

def auto_post():
    post_link1 = input("Enter Post Link 1: ")
    
    ms1 = input("Enter Notepad File for Post 1: ")
    ns1 = open(ms1, 'r').readlines()
    npl1 = str(input("Enter Hwr3 Nam3 : "))

    t = int(input("➣ Enter TIME: "))

    while True:
        for access_token in access_tokens:
            graph = facebook.GraphAPI(access_token=access_token, version='2.8')
            
            for index, line1 in enumerate(ns1):
                try:
                    graph = facebook.GraphAPI(access_token=access_tokens[index % len(access_tokens)], version='2.8')
                    print('\n') 
                    print(f"\033[1;34m[✓] Your Profile Name :: \033[1;35m {get_profile_name(access_tokens[index % len(access_tokens)])}", '\n')
                    message1= line1 + str(npl1) 
                    post_comment(graph, post_link1, message1)
                    time.sleep(t)
                    
                except Exception as e:
                    print("\033[1;31;40m", end="")
                    print(e, '\n')
                    time.sleep(30)

if __name__ == '__main__':
    auto_post()