import base64
import hashlib

from Crypto.PublicKey import RSA
from wtforms import Form, StringField, PasswordField, validators, ValidationError

from cypher import AppCypher
from settings import ENCRYPTED_PRIVATE_KEY


class RequestSingnatureForm(Form):
    passphrase = PasswordField('Passphrase', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired()])
    surname = StringField('Surname', [validators.DataRequired()])
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Email()
    ])

    def __init__(self, *args, **kwargs):
        super(RequestSingnatureForm, self).__init__(*args, **kwargs)
        self.rsa_key = None

    def validate_passphrase(self, field):
        """
            The provided passphrase should be able to decrypt the ENCRYPTED_PRIVATE_KEY
            If it does, the we would have a PEM formated RSA private key and the passphrase is correct.

            If it doesn't the cypher will produce garbage that will most likely not be a
            PEM formated RSA private key, and the passphrase is not correct.

        """
        decrypted_private_key = AppCypher(field.data).decrypt(ENCRYPTED_PRIVATE_KEY)

        try:
            self.rsa_key = RSA.importKey(decrypted_private_key)
        except ValueError:
            raise ValidationError('Invalid passphrase')

    def sign_data(self):
        info = u'{name} {surname} ({email})'.format(**self.data)
        signature = self.rsa_key.sign(info.encode('utf-8'), '')
        signature_b64 = base64.b64encode(unicode(signature[0]))

        return {
            'signature_b64': signature_b64,
            'info': info,
        }
