'''Find a given word in another long string'''

def find_word_in_a_sentence(word, sentense):
    """find a word in a sentense"""
    status = True
    word = word.replace(' ', '').lower()
    sentense = sentense.replace(' ', '').lower()
    for char_in_word in word:
        lst = [pos for pos, char in enumerate(sentense) if char == char_in_word]
        if len(lst) <= 0:
            status = False
            break
    return status

if __name__ == "__main__":
    USER_WORD = input("Enter a word to search: ")
    USER_SENTENSE = input("Enter a sentense where the word to be searched: ")
    if find_word_in_a_sentence(USER_WORD, USER_SENTENSE):
        print('"{0}" is identified in sentense "{1}"'.format(USER_WORD, USER_SENTENSE))
    else:
        print('"{0}" is NOT in sentense "{1}"'.format(USER_WORD, USER_SENTENSE))
