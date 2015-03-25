import base64
import json

from flask import request
from flask.views import MethodView
from Crypto.PublicKey import RSA

from cypher import AppCypher


PRIVATE_KEY_RAW = 'Itsa me! Luigi!!!'
RSA_KEY_PAIR = RSA.generate(1024, e=65537)
ENCRYPTED_PRIVATE_KEY = AppCypher(PRIVATE_KEY_RAW).encrypt(RSA_KEY_PAIR.exportKey("PEM"))


class PassphraseSing(MethodView):

    def get(self):
        """
            This is where the single page application is served

        """
        return 'TBD'

    def post(self):
        """
            Uses form data and uses the provided passphrase to sing the person data

        """

        data = json.loads(request.data)
        passphrase = data.get('passphrase', '')

        decrypted_private_key = AppCypher(passphrase).decrypt(ENCRYPTED_PRIVATE_KEY)

        try:
            rsa_key = RSA.importKey(decrypted_private_key)
        except ValueError:
            return json.dumps({
                'error': 'Invalid passphrase',
                'success': False
            })

        info = '{name} {surname} ({email})'.format(**data)

        signature_b64 = base64.b64encode(str(rsa_key.sign(info, '')[0])),

        return json.dumps({
            'signature_b64': signature_b64,
            'info': info,
            'success': True
        })


