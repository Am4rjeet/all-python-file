import datetime
import os
import sys
from getpass import getpass
from time import sleep
import urllib3
import certifi
import warnings
from bs4 import BeautifulSoup
import mechanicalsoup

urllib3.disable_warnings()

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

response = http.request('GET', 'https://m.facebook.com')

soup = BeautifulSoup(response.data, 'html.parser')

browser = mechanicalsoup.StatefulBrowser()

# Set user agent
browser.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})

# Disable SSL verification
browser.session.verify = False

# Set URL
url = 'https://m.facebook.com/login.php'

mip='https://m.facebook.com/'

def openlink(msg4):
	response = browser.open(msg4)


  
print("\033[1;36;40m", end = "")      
   
def aclass():
    browser.open(url)
    browser.select_form(nr = 0)
    browser['email'] = email
    browser['pass'] = password
    response = browser.submit_selected()
    browser.select_form(nr = 0)
    code = str(input('Enter 2FA code: '))
    browser['approvals_code'] = code
    browser.submit_selected()
    browser.select_form(nr = 0)
    browser.submit_selected()
 
def poct(comment):

    browser.select_form(nr = 0)

    browser.form['comment_text'] = comment

    response = browser.submit_selected()
    
print("\033[1;36;40m", end = "")   

email = str(input('Enter email: '))
password = str(input('Enter password: '))
  
aclass()  

print("\033[1;33;40m", end = "")

msg4=str(input("➣Enter post link : "))

np=str(input("➣Enter kidx Name : "))

msg5=str(input("➣enter notpad file : "))

f=open(msg5, 'r')

lines = f.readlines()

f.close()

msg6= int(input("➣Enter TIME : "))

os.system('clear')

sys.stdout.flush()

print("\033[1;32;40m", end = "")

print('V3N0M W4NT3D RULL3X 4LW4YS 0N FIIR3')

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
            print (e.strftime("V3N0M W4NT3D RULL3X  ..... | DATE :: %d-%m-%Y  TIME :: %I:%M:%S %p"))            
            print(" ->Message Successfully Sent Hwrsh Rajput : : --", line, "\n")            
            count += 1            
            if count % 10 == 0:
            	sleep(1)