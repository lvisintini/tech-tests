import base64
from Crypto.Cipher import AES


class AppCypher(object):
    """
        A cypher wrapper for Crypto.Cipher.AES
        It groups togheter methods that will likely be used every time whe need
        code a message

    """

    padding_char = '#'

    def __init__(self, private_key):
        self.cypher = AES.new(self.pad(private_key))

    def pad(self, s):
        """
            Utility method to pad the length of a string to be a multiple of the cypher block size
            This is one of the restrinctions of the cypher itself

        """
        return s + self.padding_char * (AES.block_size - len(s) % AES.block_size)

    def unpad(self, s):
        """
            Removes padding chars at the right of the text.
            If the string is a decoded message and the original message ended with padding chars,
            then, the decoded message will be missing those padding chars at the end.

            The message will probably still be legible, but it wont be exactly the same as the original

        """
        return s.rstrip(self.padding_char)

    def encrypt(self, text):
        return base64.b64encode(self.cypher.encrypt(self.pad(text)))

    def decrypt(self, code):
        return self.unpad(self.cypher.decrypt(base64.b64decode(code)))