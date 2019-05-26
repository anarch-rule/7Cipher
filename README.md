# 7Cipher
A Python based brain vault system for encrypting and decrypting text data using 7 zip.

## Getting Started
Download or clone this repo.  If running on windows, .bat file and associated shortcuts are included.

### Prerequisites

Python 2.7 tested, some hooks are the for higher version.  Not fully tested on Python 3.

7 Zip Command line / 7za is required get here: [7zip Downloads.](https://www.7-zip.org/download.html)
Download the: "7-Zip Command Line Version"

### Installing
Python must be installed correctly, so when you type 'python -v' in to the command line you get a response like: 'Python 2.7.3'
Add 7 zip command line tool to the PATH, so that typing 7za to command line executes 7z.exe.
Test to see if 7zip command line is installed correctly by typing '7za' into command line, you will get a response of available commands.

Dependencies:
  pip install pycrypto
  pip install pyperclip

There are 3 .bat files:
  1. 'CreateKeyData.bat': Create a key / encrypted cipher key json file.
  2. '7Cipher_Lock.bat': Create a lock / encrypted json file.
  3. '7Cipher_Unlock.bat': Unlock / decrypt a json file.
  4. '7Cipher_Key.bat': Copy cipher key to clipboard for 10 seconds.
  
  Create shortcuts for each .bat, put the shortcuts on your desktop.  Unique image / .ico are included to set unique image for each shortcut.

## Running
Modifying .bat files on windows:
For each .bat file
  1. Change path of python: 'c:\python27\python.exe', if it is in a different location.
  2. Change the path of the 7Cipher: 'C:\7Cipher\SevenCipher.py' repo to match where you have the files located.
Create a shortcut for each .bat file, copy them to desktop.
Run CreateKeyData.bat first for initial setup.

On Windows Command Line:
Initial Setup and New Key Creation
----------------------------------
in the search bar type 'cmd'
if repo downloaded to C drive, type: 'cd C:/7Cipher-master'
type: 'python CreateKeyData.py'  Follow instruction in creating first cipher key.

Encrypting Text
----------------------------------
if repo downloaded to C drive, type: 'cd C:/7Cipher-master'
type: 'python SevenCipher.py -lock'  
  1. Load key and data directories, set the file name as prompted.
  2. Type text you wish to encrypt into the text field, push 'encrypt' button
  
Decrypting Text
----------------------------------
if repo downloaded to C drive, type: 'cd C:/7Cipher-master'
type: 'python SevenCipher.py -unlock'  
  1. Load key and data files as prompted.
  2. Click into text field and decypted text will appear.

See this video for use:

## Personalizing
GUI was created using [Page](https://sourceforge.net/projects/page/), a simple and good, tkinter based gui editor for python. Open SevenCipher.tcl with page to customize ui.
Page requires [Active TCL](https://www.activestate.com/products/activetcl/) to run.  Download it first, and then page.

GnomicKey.py --> Method: Shape() is the algorithm that constructs the cipher key.  You should customize this algorithm and make your own unique version.

## License
Free to use and modify for purposes of keeping your data secure and away from the oligarchy.

