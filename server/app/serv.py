import random,time,binascii
from Crypto.PublicKey import RSA
from Crypto import Random
from utils import *


def import_key(filename):
    data=txt_r(filename)
    key=RSA.importKey(data)
    return key
def rsa_encrypt(key,data):
    return key.encrypt(data,32)
def rsa_decrypt(key,encdata):
    return key.decrypt(encdata)


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

def rsa_example():
    size = 4096
    Alice = rsa_key()
    Alice.gen_key(size)
    #Alice.import_key('alice_'+str(size)+'.asc')
    Bob = rsa_key()
    Bob.gen_key(size)
    #Bob.import_key('bob_'+str(size)+'.asc')
    Alice_pub = Alice.public_key
    Bob_pub = Bob.public_key
    Alice.export_private_key('alice_'+str(size)+'.asc')
    Bob.export_private_key('bob_'+str(size)+'.asc')

    t = time.time()
    data = 'HIIII' #read_file('PAD 2016-09-01.ecp')
    print data
    print len(data)
    hash = sha512(data)
    encdata = Bob.encrypt(data)
    #print encdata
    t2=time.time()
    print 'Encryption Time',t2-t
    t=time.time()
    signature=Alice.sign(hash)
    #print signature
    t2=time.time()
    print 'Signature Time',t2-t
    be = binascii.b2a_base64(encdata[0])

    t=time.time()
    decdata = Bob.decrypt(encdata)
    hash = sha512(decdata)
    verify = Alice.verify(hash,signature)
    print'VERIFY',verify
    print decdata
    t2=time.time()
    print 'Decryption Time',t2-t

#a=rsa_example()
serv = rsa_key()
serv.import_key('server_4096.asc')
encfile = read_file('enckey')
deckey = serv.decrypt(binascii.a2b_base64(encfile))
print deckey
