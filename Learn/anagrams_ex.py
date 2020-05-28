'''Example of anagram'''

def is_anagram_words(input_1, input_2):
    """Check whether both given inputs are anagram"""
    status = True
    input_1 = input_1.replace(' ', '').lower()
    input_2 = input_2.replace(' ', '').lower()
    if len(input_1) != len(input_2):
        return False
    for char_1 in input_1:
        if char_1 not in input_2:
            status = False
            break
        if input_1.count(char_1) != input_2.count(char_1):
            status = False
            break

    return status

if __name__ == "__main__":
    USER_INPUT_1 = input("Enter 1st word to check whether it is Anagram:")
    USER_INPUT_2 = input("Enter 2nd word to check whether it is Anagram:")
    if is_anagram_words(USER_INPUT_1, USER_INPUT_2):
        print('Yes "{0}" & "{1}" is Anagram'.format(USER_INPUT_1, USER_INPUT_2))
    else:
        print('No "{0}" & "{1}" is NOT Anagram'.format(USER_INPUT_1, USER_INPUT_2))
