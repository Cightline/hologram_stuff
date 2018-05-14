
import rsa
from os.path import exists

def get_pub_key():

    path = '/etc/quasar/public_key.pem'

    if not exists(path):
        return False

    with open(path, 'r') as pub_:
        return rsa.PublicKey.load_pkcs1(pub_.read())

def get_priv_key():
    path = '/etc/quasar/private_key.pem'

    if not exists(path):
        return False

    with open(path, 'r') as priv_:
        return rsa.PrivateKey.load_pkcs1(priv_.read())





if __name__ == '__main__':
    print(get_pub_key())
    print(get_priv_key())
