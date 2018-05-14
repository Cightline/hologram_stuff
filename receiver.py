from Hologram.HologramCloud import HologramCloud

from json   import loads, dumps
from base64 import b64decode

import paho.mqtt.client as mqtt

from rsa    import verify 
from config import get_config
from time   import sleep
from key_tools import get_pub_key

cfg = get_config()

credentials = {'devicekey': cfg['nova-device-key']}

hologram = HologramCloud(credentials, network='cellular')
hologram.enableSMS()

public_key = get_pub_key()

if not public_key:
    print('Unable to load public key')
    exit(1)

def handle_message():

    sms_obj = hologram.popReceivedSMS()

    if sms_obj:
        try:
            m = loads(sms_obj.message)

            sig = b64decode(m['s'])
            msg = m['m']

            sig_status = verify(dumps(msg), sig, public_key)

            if not sig_status:
                print('invalid signature:', sms_obj.message)
                return 


            print('valid signature:', sms_obj.message)

            if 't' not in msg:
                print('no topic in message')
                return 

            if 'v' not in msg:
                print('no value in message')
                return

            client.publish('nova/%s' % (msg['t']), msg['v'])

        except Exception as e:
            print('exception:', e)




def on_connect(client, userdata, flags, rc):
    print('connected with result code: %s' % (rc))

def on_message(client, userdata, msg):
    print('message:', msg)


def on_disconnect(client, userdata, rc):
    print('disconnected...')


client = mqtt.Client()
client.on_connect    = on_connect
client.on_message    = on_message
client.on_disconnect = on_disconnect

client.connect_async("localhost", 1883, 60)

client.loop_start()

while True:
    handle_message()
    sleep(1)
