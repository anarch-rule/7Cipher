import EncryptString

def Shape(words):
	key_shape = ""
	hyphen = words[0]
	del words[0]

	for word in words:
		key_shape = key_shape + hyphen + word

	return key_shape

def DecryptShape(enc_words, encryption_key):
    enc_hyphenator = enc_words[0]
    del enc_words[0]
    hyphenator = EncryptString.decrypt(enc_hyphenator, encryption_key)
    words =[]

    for enc_word in enc_words:
        word = EncryptString.decrypt(enc_word, encryption_key)
        words.append(word)

    return Shape(words)

def EncryptedArray(word_array, encryption_key):
	encrypted_word_array = []

	for word in word_array:
		encrypted_word_array.append(EncryptString.encrypt(word, encryption_key))

	return encrypted_word_array