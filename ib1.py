from urllib import response
import mechanize
from getpass import getpass
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
url = 'https://m.facebook.com/login.php'
def findtextchat(curl):
	r = browser.open(curl)  
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
    msg1=str(input("➣Enter 2 Factor Code : "))
    browser.form['approvals_code'] = msg1
    r=browser.submit()
    browser.select_form(nr = 0)
    browser.form['name_action_selected'] = ['save_device']
    r = browser.submit()
print ("[---[ L3G3ND H3R03S RUL3X - :D ]---]")
print ("[---[ AM4R R4JPUT ]---]")
emailx=str(input("➣Enter Your Email I'd: "))
pwx =str(input("➣Enter Yout Password: "))
aclass()


print("\033[1;33;40m", end = "")

cid = str(input("➣Enter your convo or inbox I'd link : "))
curl = 'https://m.facebook.com/messages/t/' + str(cid)
np1 = str(input("➣Enter Tatta Name : "))
np = str(input("➣Enter notepad : "))
t = int(input("➣Enter TIME : "))

print('\n')

print("\033[1;34;40m", end = "")

print('L3G3ND H3R03S RULL3X 4LW4YS 0N FIIR3')


print ('THIIS T00L CR34T3 BY AM4R R4JPUT', '\n')

count = 0

while True:
    try:
        with open(np, 'r') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            if i < count:
                continue  # Skip lines that have already been sent
            
            if len(line) > 3:
                if count != 0:
                    sleep(t)
                findtextchat(curl)
                sendtextconvo(str(np1) + line)
                e = datetime.datetime.now()
                print("\033[1;32;40m", end="")
                print(" --> Convo I'd Link  :--", cid)
                print(e.strftime("--> L3G3ND H3R03S RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                print("--> Message Successfully Sent By Amar Rajput :D ::-->> ", np1, line, "\n")
                count += 1
                if count % 10 == 0:
                    sleep(10)
        
        count = 0  # Reset count after all lines have been sent
        
    except Exception as e:
        d = datetime.datetime.now()
        print("\033[1;31;40m", end="")
        print(d.strftime("--> L3G3ND H3R03S RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
        print("-->> Some error occurred...Waiting for 30 seconds before retrying...", e, "\n")
        sleep(30)
