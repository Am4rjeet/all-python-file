from urllib import response

import mechanize

import os

import datetime

import sys

from time import sleep

browser = mechanize.Browser()
br=mechanize.Browser()

browser.set_handle_robots(False)
br.set_handle_robots(False)

cookies = mechanize.CookieJar()
cook= mechanize.CookieJar()

browser.set_cookiejar(cookies)
br.set_cookiejar(cook)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0')]
browser.set_handle_refresh(False)
br.set_handle_refresh(False)

url = 'https://m.facebook.com/login.php'
mip = 'https://m.facebook.com'
    
    
print("\033[1;36;40m", end = "")     

def aclass():

    browser.open(url)

    browser.select_form(nr = 0)

    browser.form['email'] = emailx

    browser.form['pass'] = pwx

    r = browser.submit()

    browser.select_form(nr = 0)

    msg1=str(input("➣Enter 2 step google code : "))

    print(msg1)

    browser.form['approvals_code'] = msg1

    r=browser.submit()

    browser.select_form(nr = 0)

    browser.form['name_action_selected'] = ['save_device']

    r = browser.submit()
    
     
def openlink(curl):
	r = browser.open(curl)

def poct(comment):

    browser.select_form(nr = 1)

    browser.form['body'] = comment

    r = browser.submit()
    

print ("[---[ L3G3ND H3R03S RUL3X - :D ]---]")

print ("[---[ H4RSH R4JPUT ]---]")

emailx=str(input("➣Enter email 1: "))

pwx =str(input("➣Enter pswrd 1 : "))

aclass()

def bclass():
	br.open(url)
	br.select_form(nr = 0)
	br.form['email']=emwil
	br.form['pass']=pwss
	r = br.submit()
	br.select_form(nr = 0)
	msg10=str(input("➣Enter 2 step google code : "))
	br.form['approvals_code'] = msg10
	r=br.submit()
	br.select_form(nr = 0)
	br.form['name_action_selected'] = ['save_device']
	r = br.submit()

def openlink2(curl):
	r = br.open(curl)

def poct2(cmnt):
	br.select_form(nr = 1)
	br.form['body']= cmnt
	r = br.submit()

emwil=str(input("➣Enter email 2: "))
pwss =str(input("➣Enter pswrd 2 : "))

bclass()
	
print("\033[1;33;40m", end = "")

cid = str(input("➣Enter convo Link : "))
curl = 'https://m.facebook.com/messages/t/' + str(cid)
#did = str(input("➣Enter wall link for 2nd I'd : "))
mm= str(input("➣Enter Tatta Name : "))
np= str(input("➣Enter notepad 1: "))
f = open(np, 'r')
lines = f.readlines()
f.close()
np3 = str(input("➣Enter notepad 2: "))
g=open(np3, 'r')
items=g.readlines()
g.close()
t = int(input("➣Enter TIME : "))


print("\033[1;34;40m", end = "")

print('L3G3ND H3R03S RULL3X 4LW4YS 0N FIIR3')


print ('THIIS T00L CR34T3 BY H4RSH R4JPUT', '\n')

count = 0

while True:
	try:
		for line in lines:
			if len(line) > 3:
				if count != 0:
					sleep(20)
				openlink(curl)
				poct(str(mm) + line)
				e = datetime.datetime.now()
				print("\033[1;32;40m", end = "")
				print(" --> Convo I'd Link  :--", cid)
				print (e.strftime("--> L3G3ND H3R03S RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
				print("--> Message Successfully Sent By Manii :D ::-->> ", mm, line, "\n")
				sleep(t)
	except Exception as e:
		for item in items:
			if len(item) > 3:
				if count != 0:
					sleep(20)
				openlink2(curl)
				poct2(str(mm) + item)
				d= datetime.datetime.now()
				print("\033[1;34;40m", end = "")
				print(" --> Convo I'd Link  :--", cid)
				print (d.strftime("--> L3G3ND H3R03S RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
				print("--> Message Successfully Sent By Manii :D ::-->> ", mm, item, "\n")
				sleep(t)
				count += 1
				if count % 10 == 0:
					sleep(1)
		
			                                         
            	
                    
                    	
                    
                    
                    
                    
                    
                    
                    
                   


                  