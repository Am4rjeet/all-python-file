import os, sys, requests, re, random, time
import datetime
import getpass
from os import system as psl
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as bsn
from platform import system
import sys
import os
import datetime   
from time import sleep

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



def message_on_messenger(message):
    for index, i in enumerate(ns):
        try:
            ses = requests.Session()
            cookies={'cookie': cookies_files[index % len(cookies_files)]}
            message = i + str(np)
            g_url = 'https://mbasic.facebook.com/'+lnk
            g_headers = {
                'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'referer': 'https://mbasic.facebook.com/'+lnk,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
             }   
            res1 = requests.get(url=g_url, cookies=cookies, headers=g_headers).text
            j2 = re.search(r'name="jazoest" value="([^"]+)"', res1).group(1)
            fb_dtsg = re.search(r'name="fb_dtsg" value="([^"]+)"', res1).group(1)
            
            ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
            rose1 = sop(res1, 'html.parser')
            rose = rose1.find('form', method='post')['action']
            payload = {
                'fb_dtsg': fb_dtsg,
                'jazoest': j2,
                'comment_text': str(message),
                'send': 'Comment',
            }
            host = 'https://mbasic.facebook.com'
            post = ses.post(url=host+rose, data=payload, cookies=cookies).text
            e =datetime.now()
            print('\033[1;34m[✓] Your Active Page Name :: \033[1;35m', get_user_info(cookies_files[index % len(cookies_files)]))
            print('\n')
            print("\033[1;32;40m", end = "")
            print("--> Your Post Link  :--", lnk)
            print (e.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
            print("--> Message Successfully Sent By HwRsH Rajput :D ::-->> ", message, "\n")
            time.sleep(timm)            
            
            print('\n')

        except Exception as e:
            print("\033[1;31;40m", end="")
            g =datetime.now()
            print (g.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
            print("--> Kuch Error Fine Huii Hx ::-->> ", e, "\n")
            time.sleep(30)

def get_user_info(cookie):
    try:
        user_info = {}
        url = 'https://mbasic.facebook.com/me'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        cookies = {'cookie': cookie}
        response = requests.get(url, headers=headers, cookies=cookies)
        soup = sop(response.content, 'html.parser')
        user_info = soup.find('title').text.strip()
        return user_info
    except Exception as e:
        print("\033[1;31m[×] Error fetching user information, Please Check Your Account Data : ", e)
        return None


def get_messages():
    try:
        url = "https://www.facebook.com"
    except HTTPError as e:
        print("HTTP Error")
    except URLError as e:
        print("URL Error")

if __name__ == "__main__":
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    print('''\033[1;35m-=[ Facebook Tool Pool Ka Super Hero Venom Wanted Rullex ]=-''')
    print('''\033[1;33m-=[ Contact Us :: https://www.facebook.com/your.dad.harsh/]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;32m[#] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[#] _ Tool Fucker == > [ Harsh Rajput ]\n''')
    print("\033[1;36;40m", end = "")
    mo = str(input("\033[1;36m[+] Mobile Number :: "))
    cookies_file = input('[+] Enter Your Page Data : ')
    print('\n')

    with open(cookies_file, 'r') as f2:
        cookies_files = f2.read().splitlines()


    for index, cookies in enumerate(cookies_files, 1):
        user_info = get_user_info(cookies)
        if user_info is not None:
        	print(f"\033[1;32m{index}. Your Page Name :: \033[1;35;1m {user_info}")
        	
        


    for cookies in cookies_files:
        
        print('\n')
    
        lnk = input("\033[1;36m[+] Enter Wall Link :: \033[1;32;1m")

        
        np = input("\033[1;36m[+] Enter Hwr3 :: \033[1;32;1m")

        ms = input(BOLD + CYAN + "\033[1;36m[+] Enter Notepad File :: \033[1;32;1m")
        lim = int(input("\033[1;36m[+] File Repeat No :: \033[1;32;1m"))
        timm = int(input(BOLD + CYAN + "\033[1;36m[+] Speed in Seconds :: \033[1;32;1m"))
        print('\n')               
        
        ns = open(ms, 'r').readlines()

        for i in range(lim):
            message_on_messenger(lnk)