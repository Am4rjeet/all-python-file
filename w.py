from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Twilio WhatsApp sandbox number
from_whatsapp_number='whatsapp:+918000294846

# Prompt user to enter their WhatsApp number
to_whatsapp_number = input("Enter your WhatsApp number (including country code): ")

# Initialize Twilio Client
client = Client(account_sid, auth_token)

try:
    # Request WhatsApp authentication code
    verification = client.verify \
                            .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                            .verifications \
                            .create(to='whatsapp:' + to_whatsapp_number, channel='whatsapp')
    print(f"Authentication code sent to {to_whatsapp_number}.")
    
    # Prompt user to enter the received authentication code
    code = input("Enter the authentication code received: ")
    
    # Verify the WhatsApp number with the entered code
    verification_check = client.verify \
                                .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                                .verification_checks \
                                .create(to='whatsapp:' + to_whatsapp_number, code=code)
    
    if verification_check.status == 'approved':
        print("WhatsApp number verified successfully!")
    else:
        print("Verification failed. Please check the entered code.")
except Exception as e:
    print(f"Error: {e}")