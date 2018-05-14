
import rsa

def get_pub_key(path):
    with open(path, 'r') as pub_:
        return rsa.PublicKey.load_pkcs1(pub_.read())

def get_priv_key(path):
    with open(path, 'r') as priv_:
        return rsa.PrivateKey.load_pkcs1(priv_.read())





if __name__ == '__main__':
    import os
    cd = os.getcwd()
    print(get_pub_key('%s/public_key.pem' % (cd)))
    print(get_priv_key('%s/private_key.pem' % (cd)))
