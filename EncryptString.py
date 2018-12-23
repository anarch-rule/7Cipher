# A simple class for encrypting text no larger than 32 chars
#into readable cipher text using a password / cipher key.
#Slightly modified version of this: https://paste.ubuntu.com/11024555/

import struct
from Crypto.Cipher import AES
import base64


def pad16(s):
    t = struct.pack('>I', len(s)) + s
    return t + '\x00' * ((16 - len(t) % 16) % 16)


def unpad16(s):
    n = struct.unpack('>I', s[:4])[0]
    return s[4:n + 4]


class Crypt(object):
    def __init__(self, password):
        password = pad16(password)
        self.cipher = AES.new(password, AES.MODE_ECB)

    def encrypt(self, s):
        s = pad16(s)
        return base64.b64encode(self.cipher.encrypt(s))

    def decrypt(self, s):
        t = self.cipher.decrypt(base64.b64decode(s))
        return unpad16(t)


def encrypt(s, p):
    c = Crypt(p)
    return c.encrypt(s)


def decrypt(s, p):
    c = Crypt(p)
    return c.decrypt(s)