from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()

browser.set_handle_robots(False)

cookies = mechanize.CookieJar()

browser.set_cookiejar(cookies)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]

browser.set_handle_refresh(False)

url = 'https://mbasic.facebook.com/login.php'

def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        sleep(0.03)
        
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def findtextchat(curl):
	r = browser.open(curl)
	def findtextchat(curl2):
		r = browser.open(curl2)
		def findtextchat(curl3):
			r = browser.open(curl3)
			
    
def sendtextconvo(comment):
	browser.select_form(nr = 1)
	browser.form['body'] = comment
	r = browser.submit()
	
    
print("\033[1;36;40m", end = "")    

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    msg1=str(input("➣Enter 2 Factor Authentication Code : "))

    print('\n')
    
    print("\033[1;34;40m", end = "")
    
    sp('''\n++++ C0NGR4TUL4TI0NS ++++
++++ Y0UR I'D SUCC33SFULLY L0GIN ++++ \n''')

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()

    
    print("\033[1;34;40m", end = "")    
    

print("\033[1;33;40m", end = "")

print('''
--------------------------------------------------------------------------------------------------------------------------------''')

    
 
print("\033[1;32;40m", end = "")

sp("\n[---[ V3N0M W4NT3D RUL3X - :D ]---] \n")

sp("\n[---[ Amarjeet ]---] \n")

print('\n')

print("\033[1;36;40m", end = "")

emailx=str(input("➣Enter Your Email I'd : "))

pwx =str(input("➣Enter Your Password : "))

print("\033[1;34;40m", end = "")

sp('\n[==[ ++++ W4IT F0R 30 S3C0ND ++++ ]==] \n')

print()

print("\033[1;36;40m", end = "")


aclass()

print('\n')

print("\033[1;31;40m", end = "")

sp('''\n [[ +---+ [[ I'D R34DY F0R RUNNING ]] +---+ ]] \n''')

print()

print("\033[1;33;40m", end = "") 

cid = str(input("➣Enter your convo or inbox I'd link 1 : "))
curl = 'https://m.facebook.com/messages/t/' + str(cid)
uid = str(input("➣Enter your convo or inbox I'd link 2 : "))
curl2 = 'https://m.facebook.com/messages/t/' + str(uid)
#did = str(input("➣Enter your convo or inbox I'd link 3 : "))
#curl3 = 'https://m.facebook.com/messages/t/' + str(did)
np1 = str(input("➣Enter 1st Convo or ib Ka Tatta Name  : "))
np2 = str(input("➣Enter 2nd Convo or ib Ka Tatta Name  : "))
#np3 = str(input("➣Enter 3rd Convo or ib Ka Tatta Name  : "))
np = str(input("➣Enter notepad : "))
t = int(input("➣Enter TIME : "))

print('\n')

print("\033[1;34;40m", end = "")

sp('\nL3G3ND H3R03S 4LW4YS 0N FIIR3 \n')


sp('\nTHIIS T00L CR34T3 BY Amarjeet\n')

print('\n')

count = 0

while True:
    try:
        with open(np, 'r') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            if i < count:
                continue  # Skip lines that have already been processed

            if len(line) > 3:
                if count != 0:
                    sleep(t)
                findtextchat(curl)          
                sendtextconvo(str(np1) + line)
            
                e = datetime.datetime.now()
                print("\033[1;32;40m", end="")
                print(" --> Convo Or Inbox I'd Link 1  :--", cid)            
                print(e.strftime("--> L3G3ND H3R03S H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))            
                print("--> Message Successfully Sent By Amar Rajput :D ::- ", np1, line, "\n")
                sleep(t)
                d = datetime.datetime.now()
            
                findtextchat(curl2)
                sendtextconvo(str(np2) + line)
                print("\033[1;34;40m", end="")
                print(" --> Convo Or Inbox I'd Link 2  :--", uid)            
                print(d.strftime("--> L3G3ND H3R03S H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))            
                print("--> Message Successfully Sent By Amar Rajput :D ::- ", np2, line, "\n")               
                count += 1
                if count % 10 == 0:
                    sleep(10)
        
        count = 0  # Reset count after all lines have been sent
 
    except Exception as e:
        m = datetime.datetime.now()
        print("\033[1;31;40m", end="")
        print(m.strftime("--> L3G3ND H3R03S H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
        print("-->> Some error occurred...Waiting for 30 seconds before retrying...", e, "\n")
        sleep(30)