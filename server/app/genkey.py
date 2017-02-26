
from rsa import *

size = 1024
serv_key = RSA_key()
serv_key.gen_key(size)
serv_key.export_private_key('server_key.asc')
serv_key.export_public_key('server_public_key.asc')