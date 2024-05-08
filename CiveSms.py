import os
from twilio.rest import Client

# Twilio credentials (replace with your own)
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = ''


"""Create account Twilio get your twilio phone number..
And utapata authentication token pia, replace yakwako..
 you will also be given Sid tumia yako
Also install twilio , using pip install twilio. """

class color:
    reset = '\033[0m'
    red = '\033[31m'
    yellow = '\033[33m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    gray = '\033[90m'
    italic = '\033[3m'

def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def intro():
    cls()
    print(color.reset)
    print(f"{color.italic}{color.red}                         CiveSms. \n")
    print(f"{color.italic}{color.red}                         by Sheldon. \n")
    print(color.reset, end="")
    
    
    

def control(var, a):
    if (len(var) > 4 and a) or (not (3 <= len(var) <= 15) and not a):
        return False
    if not var.isdigit():
        return False
    return True

def sure(cc, pn, ms):
    while True:
        cls()
        intro()
        print(f"{color.cyan}    Kodi ya nchi:  {color.gray}{cc}{color.reset}")
        print(f"{color.cyan}    Namba ya simu:  {color.gray}{pn}{color.reset}")
        print(f"{color.cyan}    Ujumbe:  {color.gray}{ms}{color.reset}")
        sel = input(f"\n{color.yellow}    Thibitisha (y / n)?  {color.reset}").lower()
        if sel == 'y':
            return True
        elif sel == 'n':
            return False

def sendMessage():
    while True:
        cls()
        intro()
        countryCode = input(f"{color.cyan}    Kodi ya nchi:  {color.gray}+{color.reset}")
        if control(countryCode, True):
            break
    countryCode = '+' + countryCode
    while True:
        cls()
        intro()
        print(f"{color.cyan}    Kodi ya nchi:  {color.gray}{countryCode}{color.reset}")
        phoneNumber = input(f"{color.cyan}    Namba ya simu:  {color.reset}")
        if control(phoneNumber, False):
            break
    cls()
    intro()
    print(f"{color.cyan}    Kodi ya nchi:  {color.gray}{countryCode}{color.reset}")
    print(f"{color.cyan}    Namba:  {color.gray}{phoneNumber}{color.reset}")
    message = input(f"{color.cyan}    Ujumbe:  {color.reset}")
    if not sure(countryCode, phoneNumber, message):
        sendMessage()
    
    # Initialize Twilio client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    # Send SMS message
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=countryCode + phoneNumber
        )
        print("\n   Ujumbe umetumwa kikamilifu ! SID:", message.sid)
    except Exception as e:
        print("\n   Error:", str(e))

sendMessage()

