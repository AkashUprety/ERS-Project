import os
import math
import random    
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = "akshuprety2510@gmail.com"
to_address = "infotechtemple@gmail.com"
msg = MIMEMultipart('alternative')
msg['Subject'] = "E-gain"
msg['From'] = from_address
msg['To'] = to_address

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
username = 'akashuprety2510@gmail.com'  
password = 'wncrmrdivojbzvjg'
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.ehlo()
server.starttls()
server.login(username,password)  
server.sendmail(from_address, to_address, msg)  
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
   
elif a!=OTP:
        print("\nPlease Check your OTP again")
        a = input("Enter Your OTP Again >>: ")
        if a == OTP:
            print("Verified")
        else:
            print("Please Check your OTP again")
else:
    print("Please Check your OTP again")

server.quit()