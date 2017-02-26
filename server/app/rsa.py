import random,time,binascii
from Crypto.PublicKey import RSA
from Crypto import Random
from utils import *


class RSA_key():
    def __init__(self):
        self.hasprivate = None
        self.size = None

    def gen_key(self,size):
        self.size = size
        t = time.time()
        print 'Generating',size,'bit key'
        rand = Random.new().read
        self.private_key = RSA.generate(size, rand)
        self.public_key = self.private_key.publickey()
        self.hasprivate=True
        t2=time.time()
        print 'Generation Time',t2-t

    def export_private_key(self,filename):
        data = self.private_key.exportKey()
        write_file(data,filename)

    def export_public_key(self,filename):
        data = self.public_key.exportKey()
        write_file(data,filename)

    def import_key(self,filename):
        data = read_file(filename)
        key = RSA.importKey(data)
        if key.has_private:
            self.private_key = key
            self.public_key = key.publickey()
            self.hasprivate = True
        else:
            self.public_key = key
            self.private_key = None
            self.hasprivate = False
        self.size = key.size

    def sign(self,data):
        if self.private_key.can_sign:
            decdata = self.private_key.sign(data,'')
        else:
            decdata = None
        return decdata

    def verify(self,data,signature):
        return self.public_key.verify(data,signature)

    def encrypt(self,data):
        #Attention: this function performs the plain, primitive RSA encryption (textbook). In real applications, you always need to use proper cryptographic padding, and you should not directly encrypt data with this method. Failure to do so may lead to security vulnerabilities. It is recommended to use modules Crypto.Cipher.PKCS1_OAEP or Crypto.Cipher.PKCS1_v1_5 instead.
        if self.public_key.can_encrypt:
            encdata = self.public_key.encrypt(data,32)
        else:
            encdata = None
        return encdata

    def decrypt(self,data):
        return self.private_key.decrypt(data)