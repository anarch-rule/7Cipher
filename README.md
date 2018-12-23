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

There are 3 .bat files:
  1. Create a key / encrypted cipher key json file.
  2. Create a lock / encrypted json file.
  3. Unlock / decrypt a json file.
  
  Create shortcuts for each .bat, put the shortcuts on your desktop.  Uniqur image / .ico are included to set unique image for each shortcut.

See this video for use:

## Personalizing
GUI was created using [Page](https://sourceforge.net/projects/page/), a simple and good gui editor for python. Open SevenCipher.tcl with page to customize ui.
Page requires [Active TCL](https://www.activestate.com/products/activetcl/) to run.  Download it first, and then page.

GnomicKey.py --> Method: Shape() is the algorithm that constructs the cipher key.  You should customize this algorithm and make your own unique version.

## License
Free to use and modify for purposes of keeping your data secure and away from the oligarchy.

