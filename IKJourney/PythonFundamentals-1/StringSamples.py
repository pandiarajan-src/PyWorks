##############################################################
# Length of a last word
def length_of_last_word(sentence):
    """
    Args:
     sentence(str)
    Returns:
     int32
    """
    # Write your code here.
    return len(sentence.rstrip().split(" ")[-1])


# Length of a last word
# print(length_of_last_word("interview kickstart"))
# print(length_of_last_word(" Hello World "))
# print(length_of_last_word(""))
##############################################################

##############################################################
# Count Alphabets
def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    # Write your code here.
    count = 0
    for c in s:
        if c.isalpha():
            count += 1
    return count


# Count Alphabets
# print(count_alphabets("#aBdj12C"))
# print(count_alphabets("123 !@#$"))
# print(count_alphabets(""))
##############################################################

#############################################################
# Find first occurrence of a character in a string
def find_first_occurrence(s: str,
                          to_find: str) -> int:
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    # Write your code here.
    if len(s) == 0:
        return -1
    index = 0
    for c in s:
        if c == to_find:
            break
        index += 1
    if index >= len(s):
        return -1
    return index


# print(find_first_occurrence("interview", "e"))
# print(find_first_occurrence("kickstart", "n"))
# print(find_first_occurrence("", ""))
##############################################################

##############################################################
def reverse_words_in_string(input_words: str) -> str:
    reversed_words = input_words.split(" ")
    reversed_words.reverse()
    return ' '.join(reversed_words)


# print(reverse_words_in_string("best technical interview prep course"))
# print(reverse_words_in_string("kickstart"))
# print(reverse_words_in_string(""))
# print(reverse_words_in_string("   "))

##############################################################
# partition the string, the below returns a tuple with "best" " " "technical interview prep course"
# input_words = "best technical interview prep course"
# print(input_words.partition(" "))
##############################################################
