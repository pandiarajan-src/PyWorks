"""
Check If An Array Contains Duplicates

    Check if any element occurs more than once in a given list of numbers.
    Return true if an array contains duplicates, else return false.

    Example:
        input => "nums": [10, 30, 10, 20]
        output => true

        input => "nums": [5, 10, 15, 20]
        output => false
"""


def check_array_has_duplicate(numbers: list[int]) -> bool:
    """
    This method uses set operation to remove duplicate and compare length of array and set for results
    :param numbers: list of numbers containing duplicate
    :return: True if duplicate element exists False if not
    """
    return len(numbers) != len(set(numbers))


def check_array_has_duplicate_native(numbers: list[int]) -> bool:
    """
    This method loop through list and store in another sequence object and check for dups
    :param numbers: list of numbers containing duplicate
    :return: True if duplicate element exists False if not
    """
    dup = set()
    for num in numbers:
        if num in dup:
            return True
        else:
            dup.add(num)
    return False
