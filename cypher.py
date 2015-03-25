import base64
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA


# have more comment here !!

class AppCypher(object):
    padding_char = '-'

    def __init__(self, private_key):
        self.cypher = AES.new(self.pad(private_key))

    def pad(self, s):
        return s + self.padding_char * (AES.block_size - len(s) % AES.block_size)

    def unpad(self, s):
        return s.rstrip(self.padding_char)

    def encrypt(self, text):
        return base64.b64encode(self.cypher.encrypt(self.pad(text)))

    def decrypt(self, code):
        return self.unpad(self.cypher.decrypt(base64.b64decode(code)))


if __name__ == "__main__":
    PRIVATE_KEY_RAW = 'Itsa me! Luigi!!!'
    RSA_KEY_PAIR = RSA.generate(1024, e=65537)
    CYPHER = AppCypher(PRIVATE_KEY_RAW)
    ENCRYPTED_PRIVATE_KEY = CYPHER.encrypt(RSA_KEY_PAIR.exportKey("PEM"))
