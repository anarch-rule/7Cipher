import EncryptString

LUCKY_NUMBER = 777

def Shape(words, hyphen):
	key_shape = ""

	for word in words:
		key_shape = key_shape + hyphen + word

	key_shape = AddLuckyNumber(key_shape)

	return key_shape

def DecryptShape(enc_words, encryption_key):
    enc_hyphenator = enc_words[0]
    del enc_words[0]
    hyphenator = EncryptString.decrypt(enc_hyphenator, encryption_key)
    words =[]

    for enc_word in enc_words:
        word = EncryptString.decrypt(enc_word, encryption_key)
        words.append(word)

    return Shape(words, hyphenator)

def EncryptedArray(word_array, encryption_key):
	encrypted_word_array = []

	for word in word_array:
		encrypted_word_array.append(EncryptString.encrypt(word, encryption_key))

	return encrypted_word_array

def AddLuckyNumber(key_shape):
	"""Construct simple lucky number string
	   as an example of personalized string
	   manipulation algo. Add lucky number
	   to end of cipher text.  
    """
	key_shape = key_shape + "_" + str(LUCKY_NUMBER) + "_"
	return key_shape