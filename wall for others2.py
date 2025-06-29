import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
import mechanize
import os
import datetime
import sys
from time import sleep
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


html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legend Heroes Rullex</title>
    <style>
        body {
            background-image: url('rashmika.jpg');
            background-size: cover;
        }
    </style>
</head>
<body>
    <h1 style="color: black;">L3G3ND H3R03S RULL3X 0FFLIN3 T00L</h1>
    <p style="color: green;">This Tool Created Amarjeet</p>
    
    <p style="color: blue;">Owner Name ::- Amarjeet </p>
    
    <audio controls autoplay loop>
        <source src="https://cdn.paglasongs.com/files/sfd6/2663/Master%20the%20Blaster_320(PaglaSongs).mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
</body>
</html>
"""

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

def execute_server():
	PORT = 4000

	with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
		print("Offline Loader Running at http://localhost:{}".format(PORT))
		httpd.serve_forever()

def send_messages():
	

	requests.packages.urllib3.disable_warnings()

	

	headers = {
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
		'referer': 'www.google.com'
	}

	
	
	with open('mainwall.txt', 'r') as file:
		post_id = file.read().strip()
	with open('resumewall.txt', 'r') as file:
		resume_id = file.read().strip()
	with open('TokenFile.txt', 'r') as f2:
		access_tokens = f2.read().splitlines()
	with open('time.txt', 'r') as file:
		speed = int(file.read().strip())
	with open('hwrename.txt', 'r') as file:
		hwre_name = file.read().strip()
	with open('kidxname.txt', 'r') as file:
		kidxx = file.read().strip()
	def get_profile_name(access_token):
		try:
			graph = facebook.GraphAPI(access_token=access_token, version='2.8')
			user_info = graph.get_object('me')
			profile_name = user_info['name']
			return profile_name
		except Exception as e:
			print("-->> I'd Me Ya Token me Kuch Error Hai , Error Name :: ", e, "\n")
			print("\033[1;36;40m", end="")
			
	for index, access_token in enumerate(access_tokens, 1):
		profile_name = get_profile_name(access_token)
		print(f"{index}. All Profile Name : {profile_name}")
		
	def post_comment(graph, post_link, message):
		try:
			graph.put_object(parent_object='100006813250942_' + post_link, connection_name='comments', message=message)
			print("\033[1;32;40m", end = "")
			e =datetime.now()
			print("\033[1;32;40m", end = "")
			print (e.strftime("--> L3G3ND H3R03S RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
			print(f"--> Comment Successfully Sent By Amarjeet :D ::-->> {message}\n")
		except Exception as e:
			graph.put_object(parent_object='100006813250942_' + post_link, connection_name='comments', message=message)
			e =datetime.now()
			print("\033[1;32;40m", end = "")
			print (e.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
			print(f"--> Message Successfully Sent By HwRsH Rajput :D ::-->> {message}\n")
	print("\033[1;36;40m", end="")
	def auto_post():
		post_link1 = post_id
		post_link2 = resume_id
		ms1 = 'notepad.txt'
		ns1 = open(ms1, 'r').readlines()
		npl1 = hwre_name
		npl2 = kidxx
		t = speed
		while True:
			for access_token in access_tokens:
				graph = facebook.GraphAPI(access_token=access_token, version='2.8')
				for index, line1 in enumerate(ns1):
					try:
						graph = facebook.GraphAPI(access_token=access_tokens[index % len(access_tokens)], version='2.8')
						print('\n')
						print(f"\033[1;34m[✓] Your Profile Name :: \033[1;35m {get_profile_name(access_tokens[index % len(access_tokens)])}", '\n')
						message1= str(npl2) + line1 + str(npl1)
						post_comment(graph, post_link1, message1)
						
					except Exception as e:
						graph = facebook.GraphAPI(access_token=access_tokens[index % len(access_tokens)], version='2.8')
						print('\n')
						print(f"\033[1;34m[✓] Your Profile Name :: \033[1;35m {get_profile_name(access_tokens[index % len(access_tokens)])}", '\n')
						message1= line1 + str(npl1)
						print("\033[1;31m-->> Note ::- Main Wall Pe Error Aaya Ya Wall Udi is Wjh Se Second Save Wall Pr Loader Shift Done Ho Gaya \n")
						try:
							post_comment(graph, post_link2, message1)
						except Exception as e:
							print(e)
						
					time.sleep(speed)
	if __name__ == '__main__':
		auto_post()

def main():
	server_thread = threading.Thread(target=execute_server)
	server_thread.start()
	
	send_messages()

if __name__ == '__main__':
	main()
