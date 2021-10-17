
import os
import smtplib
import imghdr
from email.message import EmailMessage

Email_Address = os.environ.get('DB_USER')
Email_Password = os.environ.get('DB_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'BIsmillah ngehack NASA'
msg['From'] = Email_Address
msg['To'] = 'alifprianda.bastian@gmail.com'
msg.set_content('Ada potonya')


with open('OTW_Hack_NASA.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    print(file_type)


#with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#   smtp.login(Email_Address, Email_Password)

#    smtp.send_message(msg)