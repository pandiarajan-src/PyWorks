'''Implement Ceaser Cipher encryption and decryption
https://en.wikipedia.org/wiki/Caesar_cipher.'''

def ceaser_ciper_encryption(input_to_encode, key_length):
    """Ceaser Encryption method"""
    enc_output = chech_char = ""
    for letter in input_to_encode:
        if letter.isalpha():
            n_uni_char = ord(letter) + key_length
            chech_char = 'Z'
            if letter.islower():
                chech_char = 'z'
            if n_uni_char > ord(chech_char):
                n_uni_char -= 26
            enc_output += chr(n_uni_char)
        else:
            enc_output += letter
    return enc_output

def ceaser_ciper_decryption(input_to_encode, key_length):
    """Ceaser Encryption method"""
    enc_output = chech_char = ""
    for letter in input_to_encode:
        if letter.isalpha():
            n_uni_char = ord(letter) - key_length
            chech_char = 'A'
            if letter.islower():
                chech_char = 'a'
            if n_uni_char < ord(chech_char):
                n_uni_char += 26
            enc_output += chr(n_uni_char)
        else:
            enc_output += letter
    return enc_output

if __name__ == "__main__":
    try:
        KEY_LENGTH = int(input("Enter Key Length between 1 to 25: "))
        if(KEY_LENGTH < 1 or KEY_LENGTH > 25):
            print("Key length should be between 1 to 25")
            raise ValueError
        USER_INPUT = input("Enter a message to encode: ")
        USER_ENC_OUTPUT = ceaser_ciper_encryption(USER_INPUT, KEY_LENGTH)
        USER_DEC_OUTPUT = ceaser_ciper_decryption(USER_ENC_OUTPUT, KEY_LENGTH)
        print("User Input : {0} \nEncoded Output : {1} \nDecoded Output : {2}"\
                    .format(USER_INPUT, USER_ENC_OUTPUT, USER_DEC_OUTPUT))
    except ValueError:
        print("input value error, please ensure that it is proper")
    except Exception as ex_val: #pylint: disable=broad-except
        print("Unknow error happend on main : {0}".format(ex_val.__str__))
    else:
        print("***Thanks***")
