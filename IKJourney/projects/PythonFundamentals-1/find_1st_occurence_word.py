# region Find first occurrence of a character in a string

# Find first occurrence of a character in a string
# Find the first occurrence of a given character in a given string.
# Example:
#   Input => {
#                "s": "interview",
#                "to_find": "e"
#              }
#   Output => 3
#
#   Input => {
#               "s": "kickstart",
#               "to_find": "n"
#             }
#   Output => -1
# Notes
#   1. Return -1 if the character is not present.

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

# endregion
