"""
Solution for part 1, template for part 2
Using substitution ciphers to encrypt and decrypt plain text
"""


# Part 1 - Use a dictionary that represents a substition cipher to 
# encrypt a phrase

# Example of a cipher dictionary 26 lower case letters plus the blank
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

def encrypt(phrase, cipher_dict):
    """
    Take a string phrase (lower case plus blank) 
    and encrypt it using the dictionary cipher_dict
    """
    len_of_phrase = len(phrase)
    encrypt_phrase = ''
    for char_num in range(len_of_phrase):     
            encrypt_phrase = encrypt_phrase + cipher_dict[phrase[char_num]]
    return encrypt_phrase

# Tests
print("Output for part 1")
print(encrypt("pig", CIPHER_DICT))
print(encrypt("hello world", CIPHER_DICT))
print()

# Output for part 1
#vif
#hunnybtygnd






# Part 2 - Compute an inverse substitution cipher that decrypts
# an encrypted phrase

def make_decipher_dict(cipher_dict):
    """
    Take a cipher dictionary and return the cipher
    dictionary that undoes the cipher
    """
    decipher_dict={}
    for keys in cipher_dict:
        decipher_dict[cipher_dict[keys]] = keys
    return decipher_dict

DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)

# Tests - note that applying encrypting with the cipher and decipher dicts
# should return the original results
print("Output for part 2")
print(DECIPHER_DICT)
print(encrypt(encrypt("pig", CIPHER_DICT), DECIPHER_DICT))			      # Uncomment when testing
print(encrypt(encrypt("hello world", CIPHER_DICT), DECIPHER_DICT))	# Uncomment when testing
print()

# Output for part 2 - note order of items in dictionary is not important
#{'p': 'f', 'n': 'l', 'm': 'a', 'i': 'i', 'd': 'd', 'x': 'k', 'b': ' ', 'l': 'v', 'f': 'g', 'o': 's', 'u': 'e', 'a': 'n', 'c': 'y', 'r': 'q', 'e': 'z', 'k': 'c', 'w': 'm', 'g': 'r', 'y': 'o', ' ': 't', 'h': 'h', 'v': 'p', 'j': 'x', 'q': 'u', 't': 'w', 's': 'b', 'z': 'j'}
#pig
#hello world


