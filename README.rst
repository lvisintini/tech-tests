Sign data app
=============

Simple app that plays around with cryptography.

I started doing this as part of an interview for a job and I decided to finish it up properly.

This is the gist of it
----------------------

``settings.py`` contains an encrypted PEM formated RSA private key.

The user should use the react interfase to provide some data along with a passphrase.

If validation for the data passes, the passphrase is used to decrypt the RSA private key and signs the data provided with it.

This signatures is then sent to the user as a response.

If the passphrase is incorrect, then the RSA private key fails to be decripted and the user is informed that such passphrase is incorrect.

*BTW*, the correct passphrase is ``Itsa me! Luigi!!!``

If you want to test the backend with a REST Client, data sent to the server must be sent in JSON format::

    {
        "surname": "Mario",
        "name": "Luigi",
        "passphrase": "Itsa me! Luigi!!!",
        "email": "luigi@bros.com"
    }

Setup Instructions
------------------

Mostly vanilla., but added here for completeness sake::

    git clone https://github.com/lvisintini/exercise-sign-data-app.git
    cd ./exercise-sign-data-app
    mkvirtualenv exercise-sign-data-app
    pip install -r requirements.txt
    python app.py

After that, put `http://127.0.0.1:8000/` into your browser thingy and you should be able to test it out yourself.

Tests
-----

There are a few. Run them with ``py.test tests.py``


Some of the resources I used
----------------------------

- Flask Documentation
- WTforms Documentation
- http://www.codekoala.com/posts/aes-encryption-python-using-pycrypto/
- http://stackoverflow.com/questions/4232389/signing-and-verifying-data-using-pycrypto-rsa
