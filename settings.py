from Crypto.PublicKey import RSA

from cypher import AppCypher

# For the purposes of this exercise, I'm not allowed to use the following
# settings in the rest of the code base.

PRIVATE_KEY_RAW = 'Itsa me! Luigi!!!'
RSA_KEY_PAIR = RSA.generate(1024, e=65537)

# The following ones are OK to use though

ENCRYPTED_PRIVATE_KEY = AppCypher(PRIVATE_KEY_RAW).encrypt(RSA_KEY_PAIR.exportKey("PEM"))