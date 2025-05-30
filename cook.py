import http.server
import socketserver
import threading
import requests
import time
from datetime import datetime

# HTML content for the web server
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Venom Wanted Rullex</title>
    <style>
        body {
            background-image: url('rashmika.jpg');
            background-size: cover;
        }
    </style>
</head>
<body>
    <h1 style="color: black;">V3N0M W4NT3D RULL3X 0FFLIN3 T00L</h1>
    <p style="color: green;">This Tool Created By Harsh Sing Rajput</p>
    <p style="color: blue;">Owner Name ::- Siddharth Raj</p>
    <p style="color: gray;">Members List ::- </p>
    <ul>
        <li style="color: black;">1. Harsh Rajput</li>
        <li style="color: purple;">2. Ashu</li>
        <li style="color: orange;">3. Saiyan</li>
        <li style="color: teal;">4. Rudra</li>
        <li style="color: navy;">5. Aariz</li>
    </ul>
    <audio controls autoplay loop>
        <source src="https://cdn.paglasongs.com/files/sfd6/2663/Master%20the%20Blaster_320(PaglaSongs).mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
</body>
</html>
"""

# HTTP server handler
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

# Function to post comments on Facebook
def post_comment(session, post_link, message):
    try:
        comment_url = f"https://graph.facebook.com/{post_link}/comments"
        payload = {'message': message}
        response = session.post(comment_url, data=payload)
        if response.status_code == 200:
            print("Message Successfully Sent:", message)
        else:
            print("Failed to send message:", response.text)
    except Exception as e:
        print("Error:", e)

def send_messages():
    requests.packages.urllib3.disable_warnings()
    
    # Load data from files
    with open('mainwall.txt', 'r') as file:
        post_id = file.read().strip()
    with open('resumewall.txt', 'r') as file:
        resume_id = file.read().strip()
    with open('cookies.txt', 'r') as f:
        cookies = f.read().strip()
    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())
    with open('hwrename.txt', 'r') as file:
        hwre_name = file.read().strip()
    with open('kidxname.txt', 'r') as file:
        kidxx = file.read().strip()

    # Prepare cookies for requests session
    cookies_dict = {}
    for cookie in cookies.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies_dict[name] = value

    session = requests.Session()
    session.cookies.update(cookies_dict)

    def auto_post():
        post_link1 = post_id
        post_link2 = resume_id
        with open('notepad.txt', 'r') as f:
            messages = f.readlines()

        while True:
            for message in messages:
                full_message = f"{kidxx} {message.strip()} {hwre_name}"
                try:
                    post_comment(session, post_link1, full_message)
                except Exception as e:
                    print("Error posting to main wall, posting to resume wall")
                    post_comment(session, post_link2, full_message)
                time.sleep(speed)

    auto_post()

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages()

if __name__ == '__main__':
    main()