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

psl('rm -rf filer.txt')
idd = []

def get_user_info(cookie):
    try:
        user_info = {}
        url = 'https://m.facebook.com/me'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        cookies = {'cookie': cookie}
        response = requests.get(url, headers=headers, cookies=cookies)
        soup = sop(response.content, 'html.parser')
        user_info['name'] = soup.find('title').text.strip()
        user_info['user_id'] = soup.find('input', {'name': 'target'}).get('value')
        return user_info
    except Exception as e:
        print("Error fetching user information:", e)
        return None


def main():
   
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    print('''\033[1;35m-=[ Facebook Tool Pool Ka Super Hero Venom Wanted Rullex ]=-''')
    print('''\033[1;33m-=[ Contact Us :: https://www.facebook.com/your.dad.harsh/]=-\n''')
    print('''\033[1;36m---------------------------------------------------------------------\n''')
    i = datetime.now()
    print(i.strftime("\033[1;32m[#] Start Time ==> %Y-%m-%d %I:%M:%S %p "))
    print('''\033[1;32m[#] _ Tool Fucker == > [ Harsh Rajput ]\n''')
    print("\033[1;36;40m", end = "")
    cookies_file = input('[+] Enter Your Login File : ')
    cookies_list = read_cookies_from_file(cookies_file)
    print('\n')
    if not cookies_list:
        print(' \x1b[1;91mFailed to read Account from the file. Make sure the file is in the correct format.\x1b[1;97m')
        os.sys.exit()
    
    print('\x1b[1;92m[=] Account Loaded Successfully\x1b[1;97m ')
    print('\n')
    for cookies in cookies_list:
        user_info = get_user_info(cookies)
        if user_info is not None:
            print(f"\033[1;32mYour Profile Name :: \033[1;35;1m {user_info['name']}")
            print(f"\033[1;32mYour User I'd     :: \033[1;35;1m {user_info['user_id']}")
           
    
    print('\n')
    
    lnk = input("\033[1;36m[+] Enter Inbox/Convo Link :: \033[1;32;1m")
    lim = int(input("\033[1;36m[+] File Repeat No :: \033[1;32;1m"))
    filee = input("\033[1;36m[+] Enter Your Sticker File Notepad :: \033[1;32;1m")
    delay = int(input("\033[1;36m[+] Speed in Seconds :: \033[1;32;1m"))
    fileee = open(filee,'r').read()
    cpy(fileee,lim)
    file = open('filer.txt','r').readlines()
    idd.append(file)
    with bsn(max_workers=30) as crack:
        print('\n')        
        
        
        for i, mess in enumerate(idd):
            coki = cookies_list[i % len(cookies_list)]
            sm = '1'
            if sm == '1':
                print(f"\033[1;34m[✓] Your Active Profile Name :: \033[1;35;1m {user_info['name']}")
                print('\n')  
                crack.submit(msg,mess,coki,lnk,delay)
        os.sys.exit()

def read_cookies_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            cookies_list = [line.strip() for line in file.readlines()]
            return cookies_list
    except Exception as e:
        print(f"Error reading cookies from file: {e}")
        return None


def msg(mess,coki,lnk,delay):
    ses = requests.Session()
    try:
        for msgs in mess:
            try:
                time.sleep(delay)             
                cookies={'cookie': coki}
                g_url = 'https://d.facebook.com/messages/read/?tid='+lnk
                g_headers = {
                    'authority': 'd.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'referer': 'https://d.facebook.com/messages/read/?tid='+lnk,
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
                j2 = re.search(
                    r'name="jazoest" value="([^"]+)"',
                    res1
                ).group(1)
        
                fb_dtsg = re.search(
                    r'name="fb_dtsg" value="([^"]+)"',
                    res1
                ).group(1)
        
                csid = re.search(
                    r'name="csid" value="([^"]+)"',
                    res1
                ).group(1)
        
                tids = re.search(
                    r'name="tids" value="([^"]+)"',
                    res1
                ).group(1)
            
                ses.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
            
                rose1 = sop(res1, 'html.parser')
                rose = rose1.find('form',method='post')['action']
                payload = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': j2,
                    'body': '',
                    'send': 'Send',
                    'tids': tids,
                    'wwwupp': 'C3',
                    'platform_xmd': '',
                    'referrer': '',
                    'ctype': '',
                    'cver': 'legacy',
                    'csid': csid,
                    'sticker_id': str(msgs),                    
                }
                host = 'https://d.facebook.com'
                post = ses.post(url=host+rose, data=payload, cookies=cookies).text
                
                e =datetime.now()
                print("\033[1;32;40m", end = "")
                print("--> Your Inbox/Convo I'd Link  :--", lnk)
                print (e.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("--> Your Sticker Successfully Send :D :: ", "\n")
            except requests.exceptions.ConnectionError:
                time.sleep(10)
                pass
            except Exception as e:
                pass
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
        pass
    except Exception as e:
        print(e) 
        
   
def cpy(fileee,lim):
    for i in range(lim):
        open('filer.txt','a').write(fileee+'\n')

main()