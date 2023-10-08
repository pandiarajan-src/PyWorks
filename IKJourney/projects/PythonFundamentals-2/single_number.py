"""
Single Number

    Given a list of numbers in which each number appears exactly twice
    except one number that appears only once.
    Find the number that appears exactly once.
    (Try solving this in linear time complexity without using any extra space!)

    Example:
        input => "arr": [2, 1, 2, 5, 1]
        output => 5

"""


def find_single_number_naive(numbers: list[int]) -> int:
    """
    Sort the input, check all odd and even indexes are same, if not the odd index is single number
    :param numbers: list containing one unique value and all rest are twice
    :return: single number
    """
    numbers.sort()
    index = 0
    while index < len(numbers) - 1:
        if numbers[index] == numbers[index + 1]:
            index += 2
            continue
        else:
            return numbers[index]
    return numbers[index]


def find_single_number_using_set(numbers: list[int]) -> int:
    """
    Convert list of numbers to unique set.
    2 multiple of sum of unique set - sum of whole list differs with the exact single number value
    :param numbers: list containing one unique value and all rest are twice
    :return: single number
    """
    return 2 * sum(set(numbers)) - sum(numbers)


def find_single_number_using_list_add_remove(numbers: list[int]) -> int:
    """
    Create a empty list, add and remove the element in the list based on its original availability
    :param numbers: list containing one unique value and all rest are twice
    :return: single number
    """
    dup = []
    for num in numbers:
        if num in dup:
            dup.remove(num)
        else:
            dup.append(num)
    return dup[0]
