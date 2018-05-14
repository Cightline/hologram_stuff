from json import dumps
import base64
import requests

# https://hologram.io/docs/reference/cloud/http/#/reference/hologram-cloud/data-engine-messages/send-sms-to-a-device

#from Hologram.HologramCloud import HologramCloud

from rsa         import sign
from config      import get_config
from twilio.rest import Client
from key_tools   import get_priv_key

cfg = get_config()

account_sid = cfg['twilio-account-sid']
auth_token  = cfg['twilio-auth-token']

n_nova   = cfg['nova-number']
n_twilio = cfg['twilio-number']


client = Client(account_sid, auth_token)

priv_key = get_priv_key('/etc/quasar/private_key.pem')

msg = {'t':'topic', 'v':'value'}
sig = base64.b64encode(sign(dumps(msg).encode('utf-8'), priv_key, 'SHA-1')).decode('utf-8')

print(sig)
#print(base64.b64decode(sig))

#int("".join(map(chr, sig)))

signed_message = dumps({'m':msg, 's':sig})


result = requests.post('https://dashboard.hologram.io/api/1/sms/incoming', data={'deviceid':cfg['nova-device-id'], 
                                                                                 'body':signed_message,
                                                                                 'apikey':cfg['hologram-api-key']})

print(result.text)

#hologram = HologramCloud(credentials, network='cellular')

#hologram.sendSMS(n_nova, signed_message)



#result = client.messages.create(to=n_nova, from_=n_twilio, body=signed_message)

