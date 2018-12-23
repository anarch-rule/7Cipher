
#  SEVEN CIPHER
#------------------
#Gnomic Key Creator
#------------------

# Anarch Rule - 2018

# This is a simple command line program used to create
# encrypted cipher seed words we will call Gnomic Key files.
# The key is essentially a way to have something that is easily
# remembered create a complex cipher text for encrypting text data
# with 7 zip.

import sys
import getpass
import time
import os
import hashlib
import JsonUtil
import EncryptString
import GnomicKey

py3 = False

if (sys.version_info > (3, 0)):
     # Python 3 code in this block
     py3 = True

basePath = os.path.dirname(os.path.abspath(__file__))


def AnarchSelf():
	"""Load anarch info at file
    """
	anarch_self = JsonUtil.GetJsonData("ANARCH_SELF.json")
	return anarch_self


def UpdateAnarchSelf(key, value):
	"""Update the anarch info file
    """
	anarch_self = AnarchSelf()
	anarch_self[key] = value
	JsonUtil.WriteJsonData(anarch_self, "ANARCH_SELF.json")


def AddLock(lock):
	"""Add a lock has to the anarch info file
    """
	anarch_self = AnarchSelf()
	anarch_self['Locks'].append(lock)

	JsonUtil.WriteJsonData(anarch_self, "ANARCH_SELF.json")


def FormatPromptText(text):
	"""Format text so it is moreadable on the command line.
    """
	time.sleep(0.25)
	return """

	""" + text +  """

	"""

def EchoInputPrompt(text):
	"""Used for prompting user with echo, so they can see what they type as an answer.
    """
	user_input = ""
	if sys.stdin.isatty():
		if py3:
			user_input = input(FormatPromptText(text))
		else:
			user_input = raw_input(FormatPromptText(text))

	return user_input


def Yes(answer):
	"""Return true if answer is yes
    """
	accepted_answers = ["y", "yes", "ok"]
	result = False

	for a in accepted_answers:
		if a == str(answer).lower():
			result = True

	return result


def No(answer):
	"""Return true if answer is no
    """
	accepted_answers = ["n", "no", "x"]
	result = False

	for a in accepted_answers:
		if a == str(answer).lower():
			result = True
			
	return result


def CreateKeyDataFiles(key_data, lock_data):
	"""Create needed data files for new key.
    """
	key_object = {}
	key_object['Words'] = key_data
	print(FormatPromptText("Creating Key data files..."))
	AddLock(lock_data)
	key_path = os.path.join(basePath, 'Generated_Keys', 'GNOMIC_KEY_' + key_name + '.json')
	JsonUtil.CreateJsonFile(key_path, key_object)
	print(FormatPromptText("'ANARCH_SELF.json' has been updated with lock data, a new key was saved to:    " + key_path))
	print(FormatPromptText(" Move:  " + key_path + "   to an external usb drive, to be used as a cipher key."))


def ConstructGnomicKeyString():
	"""Create the word array and hash the lock cipher.
    """
	key_word_array = gnomic_key_sentence.split(' ')
	gnomic_key_data = []

	encrypted_lock_text = EncryptString.encrypt(key_name, key_name)
	lock_hash = hashlib.sha256(encrypted_lock_text.encode()).hexdigest()

	key_word_array.insert(0, hyphen)
	gnomic_key_data = GnomicKey.EncryptedArray(key_word_array, encrypted_lock_text)

	print(FormatPromptText(" This is the human readable format of your gnomic key: "))
	print(FormatPromptText(GnomicKey.Shape(key_word_array)))
	print(FormatPromptText(" Copy it and store it offline, if you think you may forget the seed parts."))

	CreateKeyDataFiles(gnomic_key_data, lock_hash)

	for txt in gnomic_key_data:
		print(EncryptString.decrypt(txt, encrypted_lock_text))


def HyphenatorPrompt():
	"""Prompt the user for a hyphenator / delimiter to add Obfuscation
		to the constructed cipher text.
    """
	global hyphen
	print(FormatPromptText(" Lastly, we need a hyphenator / delimiter text to further obfuscate the key text. It can be words, numbers, punctuation or all."))
	print(FormatPromptText(" But keep in mind, it should be something you can easily remember should you lose saved data files."))
	hyphen = EchoInputPrompt(" What is your hyphenator? ")
	confirm_hyphen = EchoInputPrompt(" Do accept your hyphenator? ")

	if Yes(confirm_hyphen):
		ConstructGnomicKeyString()

	elif No(confirm_hyphen):
		print(FormatPromptText("Try again"))
		GnomicSeedPrompt()

	else:
		print(FormatPromptText("Try again"))
		GnomicSeedPrompt()


def GnomicSeedPrompt():
	"""Prompt the user to create Gnomic sentences for cipher text seeding.
    """
	global gnomic_key_sentence
	print(FormatPromptText(" Now we create our gnomic seed.  A sentence / paragraph we can easily remember, seperated by spaces.  A poem, song lyrics, a saying you are fond of."))
	gnomic_key_sentence = EchoInputPrompt(" Input your gnomic key text. ")
	print(FormatPromptText(" Please ensure the words in your seed text is free of typos, and errors.  So that you may easily recall it if need be."))
	confirm_gnomic_key = EchoInputPrompt(" Do accept your key?  ")

	if Yes(confirm_gnomic_key):
		HyphenatorPrompt()

	elif No(confirm_gnomic_key):
		print(FormatPromptText("Try again"))

		GnomicSeedPrompt()

	else:
		print(FormatPromptText("Try again"))
		GnomicSeedPrompt()


def KeyName():
	"""Prompt the user to create a name for the new key.
    """
	global key_name
	print(FormatPromptText("Ok, " + anarch + ". We must name our key. The lock's encryption password is derived from the key name."))
	time.sleep(0.25)
	key_name = EchoInputPrompt(" What will you call this key? ")
	confirm_key_name = EchoInputPrompt(" You have chosen: " + key_name + " as your key name.  Correct?")

	if Yes(confirm_key_name):
		GnomicSeedPrompt()

	elif No(confirm_key_name):
		print(FormatPromptText("Try again"))
		KeyName()

	else:
		print(FormatPromptText("Try again"))
		KeyName()


def UpdateData():
	"""We know the user, so prompt to add a new key.
    """
	update_key = EchoInputPrompt("Welcome back: " + anarch + " Would you like to add a key?")

	if Yes(update_key):
		KeyName()

	elif No(update_key):
		print(FormatPromptText("Nothing to do."))

	else:
		print(FormatPromptText("Try again"))
		UpdateData()


def Greet():
	"""Handle the barand new user data.
    """
	try:
		global anarch
		anarch = EchoInputPrompt("Welcome Anarch, how shall I refer to you? ")
		print(FormatPromptText("I may call you: " + anarch + " Is that correct?"))
		time.sleep(0.25)
		confirm_anarch = EchoInputPrompt(FormatPromptText(" Yes(y) or No(n) "))
	except Exception as error:
		print('ERROR', error) 
	else:
		time.sleep(0.5)

		if Yes(confirm_anarch):
			UpdateAnarchSelf('Anarch', anarch)
			KeyName()

		elif No(confirm_anarch):
			Greet()

		else:
			Greet()



def FillerText():
	time.sleep(1.0)

	print("            |______|______|______|______|______|______|______|")
	time.sleep(0.05)
	print("            |      |++++++|      |ANARCH|      |++++++|      |")
	time.sleep(0.05)
	print("            |      |      |******|-RULE-|******|      |      |")
			
	if AnarchSelf()['Anarch'] == "":
		Greet()
	else:
		global anarch
		anarch = AnarchSelf()["Anarch"]
		UpdateData()


def DrawAsciiTxt():
	print(""" 

			  _          _    __    _        
			 /_|  /| )  /_|  /__)  / )  )__/ 
			(  | / |/  (  | / (   (__  /  /                                
			     __             ___          
			    /__)  /  /  /  (_            
			   / (   (__/  (__ /__   2019       
			   
			   ---SEVEN  CIPHER---
			    Gnomic Key Creator

			    gno.mic
			    /`nomik/

    expressed in or of the nature of short, pithy maxims or aphorisms.
    "The rising tide will lift all ships."

    """
    )
	FillerText()


DrawAsciiTxt()
