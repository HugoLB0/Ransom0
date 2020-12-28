## Ransom0
Ransom0 is a open source ransomware made with Python, designed to find and encrypt user data. Instead of a real server, the encryption key will be send via email to your mail box.

![Message displayed when user files are encrypted](https://hugolb0.000webhostapp.com/ransom0_main.png)

## Program Structure:
the program is organised  in **three main part**:

 - **Find Files:** find files by extensions and store the path into **path.txt**
 - **Encrypt Files:** encrypt files in **path.txt**, generate **digits id**, **send key and id**
 - **Decrypt:** ask for money, wait for the key, and decrypt file if key is correct


## How to run
You need to have python3 installed and configured

 - Download the repository via git or zip
 - Install requirements: `pip install -r requirements.txt`

Before running it, you need to modify a few thing:

 1. Add your email information: ![enter image description here](https://hugolb0.000webhostapp.com/ransom0_email.png)

 

 1. I recommend running it in a testing directory, otherwise all of your file will be encrypted: ![enter image description here](https://hugolb0.000webhostapp.com/ransom0_directory.png)

3. Run it: `python ransom0.py`

## To do:
 - [x] Add logs
 - [x] Add filter to exclude system files
 - [ ] Hide logs
 - [ ] Bypass Permission 
 - [ ] Automatically  show the message on startup
 - [x] Message in a GUI windows ?
 - [ ] Generate executable from .py file for ALL operating system
 - [ ] Store email credential in files ?


## Testing
This Program have been test on:

 - **Windows 10**
 - **Mac OS Catalina 10.15.6 (19G73)**
  - **Mac OS Big Sur 11.1 (20C69)**

## DISCLAMER 
**THIS PROJECT IS FOR EDUCATION PURPOSE ONLY, DO NOT RUN IT WITHOUT PERMISSION!**
**I AM NOT RESPONSIBLE FOR ANY DAMAGE CAUSE BY THE ILLEGAL USAGE OF THIS PROGRAM**
