
# https://stuvel.eu/files/python-rsa-doc/usage.html#signing-and-verification
# https://stuvel.eu/files/python-rsa-doc/usage.html#generating-keys

import rsa
import os

(pubkey, privkey) = rsa.newkeys(512)

priv_key_name = 'private_key.pem'
pub_key_name  = 'public_key.pem'

priv_key_path  = '%s/%s' % (os.getcwd(), priv_key_name)
pub_key_path   = '%s/%s' % (os.getcwd(), pub_key_name)


if os.path.exists(priv_key_name):
    print(priv_key_path, 'already exists')
    exit()

with open(priv_key_path, 'w') as priv_key:
    priv_key.write(privkey.save_pkcs1().decode('utf-8'))

if os.path.exists(pub_key_path):
    print(pub_key_path, 'already exists')
    exit()

with open(pub_key_path, 'w') as pub_key:
    pub_key.write(pubkey.save_pkcs1().decode('utf-8'))


#message = 'test'.encode('utf-8')
#signature = rsa.sign(message, privkey, 'SHA-1')
