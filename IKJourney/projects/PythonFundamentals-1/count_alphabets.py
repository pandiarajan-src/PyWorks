# region Count Alphabets

# Count Alphabets
# Count the number of alphabets in a given string.
# Example
#   Input =>  "#aBdj12C"
#   Output => 5
#
#   Input => "123 !@#$"
#   Output => 0
# Notes
#   String contains lower case and upper case English alphabets, digits, and some special characters

def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    count = 0
    for c in s:
        if c.isalpha():
            count += 1
    return count


# endregion