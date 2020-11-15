
def cipher(text, shift, encrypt=True):
    """
    Encrypt (decrypt) a text (ciphertext) into ciphertext (text)
    :param text: The plaintext or ciphertext
    :param shift: The shift that encrypts the text
    :param encrypt: True for encryption, False for decryption
    :return: ciphertext or plaintext

    >>> plain_text = 'this is a message.'
    >>> cipher_text = cipher(plain_text, 5, True)
    >>> cipher_text
    'ymnx nx f rjxxflj.'
    >>> new_plain_text = cipher(cipher_text, 5, False)
    >>> new_plain_text
    'this is a message.'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]

    return new_text
