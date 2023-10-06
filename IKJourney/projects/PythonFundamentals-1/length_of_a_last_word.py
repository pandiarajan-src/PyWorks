# region Length of a last word

# Length of a last word
# Find the length of the last word in a given sentence.
# Example:
#   Input => "Interview Kickstart"
#   Output => 9
#
#   Input => " Hello World  "
#   Output => 5
#
#   Notes
#       A word is defined as a character sequence consisting of non-space characters only.
#       If the last word doesn't exist, output 0.
#
def length_of_last_word(sentence):
    """
    Args:
     sentence(str)
    Returns:
     int32
    """
    # Write your code here.
    return len(sentence.rstrip().split(" ")[-1])


# endregion