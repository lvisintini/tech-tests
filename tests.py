from cypher import AppCypher



class TestCypher(object):

    def test_text_same_after_decryption(self):
        original_text = 'Hello world, this is Luis Visintini'
        pk = 'Hola mundo'

        c = AppCypher(pk)

        encrypted_text = c.encrypt(original_text)

        assert encrypted_text != original_text

        decrypted_text = c.decrypt(encrypted_text)

        assert original_text == decrypted_text

    def test_cant_decrypt_without_key(self):
        original_text = 'Hello world, this is Luis Visintini'
        correct_key = 'Hola mundo'
        wrong_key = 'Adios mundo'

        c = AppCypher(correct_key)

        encrypted_text = c.encrypt(original_text)

        assert encrypted_text != original_text

        c = AppCypher(wrong_key)
        decrypted_text = c.decrypt(encrypted_text)

        assert original_text != decrypted_text
