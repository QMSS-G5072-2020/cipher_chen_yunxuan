from cipher_yc3682 import __version__
from cipher_yc3682 import cipher_yc3682

def test_version():
    assert __version__ == '0.1.0'


def test_cipher_1():
    plain_text = 'this is a message.'
    cipher_text = cipher_yc3682.cipher(plain_text, 5, True)
    assert cipher_text == 'ymnx nx f rjxxflj.'
    new_plain_text = cipher_yc3682.cipher(cipher_text, 5, False)
    assert new_plain_text == 'this is a message.'
