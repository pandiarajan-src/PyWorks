'''Identify whether the given input is polindrome'''

def is_polindrome_word(input_word):
    """Check whether the given word is polindrome or not"""
    status = True
    input_word = input_word.replace(' ', '').lower()
    index = 0
    while index < (len(input_word)/2):
        if input_word[index] != input_word[(index*-1)-1]:
            status = False
            break
        index += 1
    return status

if __name__ == "__main__":
    USER_INPUT = input("Enter a word to check whether it is Polindrome:")
    if is_polindrome_word(USER_INPUT):
        print('Yes "{0}" is Polindrome'.format(USER_INPUT))
    else:
        print('No "{0}" is NOT Polindrome'.format(USER_INPUT))
