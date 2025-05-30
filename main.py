import requests
import time
import sys
import os
import http.server
import socketserver
import threading
import facebook
from datetime import datetime

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Legend Heroes</title>
    <style>
        body {
            background-image: url('rashmika.jpg');
            background-size: cover;
        }
    </style>
</head>
<body>
    <h1 style="color: black;">L3G3ND H3R03S RULL3X 0FFLIN3 T00L</h1>
    <p style="color: green;">This Tool Created By Amar Rajput</p>
    
    <p style="color: blue;">Owner Name ::- Amarjeet</p>
    
    <p style="color: gray;">Members List ::- </p>
    <ul>
        <li style="color: black;">1. Amar Rajput</li>
        <li style="color: purple;">2. Arijeet</li>
        <li style="color: orange;">3. Rituraj</li>
        <li style="color: teal;">4. Abhishek</li>
        <li style="color: navy;">5. Ram Raj</li>        
    </ul>

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
        print(f"Offline Loader Running at http://localhost:{PORT}")
        httpd.serve_forever()

def get_profile_name(access_token):
    try:
        graph = facebook.GraphAPI(access_token=access_token, version='3.0')
        user_info = graph.get_object('me')
        profile_name = user_info['name']
        return profile_name
    except Exception as e:
        print("-->> Error in ID or Token, Error Name :: ", e, "\n")
        return None

def post_comment(graph, post_link, message):
    try:
        graph.put_comment(post_link, message)
        e = datetime.now()
        print(e.strftime("--> L3G3ND H3R03S RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
        print(f"--> Message Successfully Sent By Amar Rajput :D ::-->> {message}\n")
    except Exception as e:
        print("Error while posting comment:", e)

def send_messages():
    requests.packages.urllib3.disable_warnings()

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
    with open('notepad.txt', 'r') as file:
        messages = file.readlines()

    print("\033[1;36;40m")
    for index, access_token in enumerate(access_tokens, 1):
        profile_name = get_profile_name(access_token)
        if profile_name:
            print(f"{index}. All Profile Name : {profile_name}")

    def auto_post():
        while True:
            for access_token in access_tokens:
                graph = facebook.GraphAPI(access_token=access_token, version='3.0')
                for message in messages:
                    try:
                        profile_name = get_profile_name(access_token)
                        if profile_name:
                            print(f"\n\033[1;34m[✓] Your Profile Name :: \033[1;35m {profile_name}\n")
                            full_message = message.strip() + ' ' + hwre_name
                            post_comment(graph, post_id, full_message)
                    except Exception as e:
                        print("Error in auto_post loop:", e)
                    time.sleep(speed)

    auto_post()

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    
    send_messages()

if __name__ == '__main__':
    main()