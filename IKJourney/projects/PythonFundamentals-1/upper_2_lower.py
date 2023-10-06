# region Convert Uppercase characters to Lowercase
#
# Convert uppercase characters to a lowercase characters in a given string
#
# Examples:
#   Input => InTerView
#   Output => interview
#
#   Input => KICKSTART
#   Output => kickstart
#
def uppercase_2_lowercase(word: str) -> str:
    """
    Convert Uppercase characters to Lowercase
    :param word:
    :return:
    """
    result = ""
    for char in word:
        if char.isupper():
            result += char.lower()
        else:
            result += char
    return result

# endregion
