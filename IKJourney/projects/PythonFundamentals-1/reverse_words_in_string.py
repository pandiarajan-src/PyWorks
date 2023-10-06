# region Reverse words in string

# Reverse Words In A Given String
# Given a string s, your task is to reverse the words of s.
# Example:
#   Input =>  "best technical interview prep courses",
#   Output => courses prep interview technical best
#
#   Input => "kickstart"
#   output => kickstart

def reverse_words_in_string(words: str) -> str:
    """
    Reverse words in a given string
    :param words: str
    :return: str
    """
    reversed_words = words.split(" ")
    reversed_words.reverse()
    return ' '.join(reversed_words)


# endregion