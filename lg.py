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


def openlink(msg4):

    r = browser.open(msg4)

os.system('clear')

sys.stdout.flush()     
        	    	    
    
print("\033[1;36;40m", end = "") 

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    msg1=str(input("➣Enter 2 step google code : "))

    print('\n')
    

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()

    

    

def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    r = browser.submit()
    
    print("\033[1;34;40m", end = "")  
   
sp('''\n 


██╗░░░░░██████╗░░██████╗░██████╗░███╗░░██╗██████╗░
██║░░░░░╚════██╗██╔════╝░╚════██╗████╗░██║██╔══██╗
██║░░░░░░█████╔╝██║░░██╗░░█████╔╝██╔██╗██║██║░░██║
██║░░░░░░╚═══██╗██║░░╚██╗░╚═══██╗██║╚████║██║░░██║
███████╗██████╔╝╚██████╔╝██████╔╝██║░╚███║██████╔╝
╚══════╝╚═════╝░░╚═════╝░╚═════╝░╚═╝░░╚══╝╚═════╝░''')

print("\033[1;31;40m", end = "")

sp('''


██╗░░██╗██████╗░██████╗░░█████╗░░██████╗
██║░░██║╚════██╗██╔══██╗██╔══██╗██╔════╝
███████║░█████╔╝██████╔╝██║░░██║╚█████╗░
██╔══██║░╚═══██╗██╔══██╗██║░░██║░╚═══██╗
██║░░██║██████╔╝██║░░██║╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░''')

print("\033[1;33;40m", end = "")
print('''
--------------------------------------------------------------------------------------------------------------------------------''')

print("\033[1;32;40m", end = "")

print ("[=[ LEGEND HEROES - :D ]=]")

print ("[=[ MANI SINGH :D ]=]")

print('\n')

print("\033[1;36;40m", end = "")

emailx=str(input("➣Enter email : "))

pwx =str(input("➣Enter pswrd : "))

print("\033[1;36;40m", end = "")

aclass()

print('\n')

print("\033[1;33;40m", end = "")

msg4="894578528101813"

msg5=str(input("➣enter notpad file : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣Enter TIME : "))

print("\033[1;34;40m", end = "")

sp('\nL3G3ND H3R0S RULL3X 4LW4YS 0N FIIR3 \n')


sp('\nTHIIS T00L CR34T3 BY M4NII SIINGH\n')


count = 0

while True:

    for line in lines:

        if len(line) > 3:

            if count != 0:

                sleep(msg6)

            openlink(msg4)

            poct(line)
            
            e = datetime.datetime.now()
            
            print("\033[1;32;40m", end = "")
            
            print(" --> Your Wall Link  :--", msg4)

            print (e.strftime("L3G3ND H3R0S RULL3X H3R3 ..... | DATE :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
            
            print("Comment Successfuly Sent By Mani Siingh -> ",line, "\n")

            count += 1

            if count % 10 == 0:

                sleep(1)