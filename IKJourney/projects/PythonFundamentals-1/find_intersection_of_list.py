# region Find intersection of list
##############################################################
# Find the intersection of a two list
# Given two lists of numbers, find their intersection.
# Example: input => "a": [4, 2, 2, 3, 1], "b": [2, 2, 2, 3, 3] => Result => [2, 2, 3]
# Notes
#   1. The order of elements in the output list does not matter.
#   2. The frequency of any number in the intersection must be
#       equal to the minimum of the frequency of that number in both the given lists.
def find_intersection_of_list_naive(l1: list, l2: list) -> list:
    """
    Find the intersection of 2 given list using list comprehension
    It doesn't consider more than one element in the list
    :param l1: list
    :param l2: list
    :return: intersection list
    """
    return [x for x in l1 if x in l2]


def find_intersection_of_list_detailed(l1: list, l2: list) -> list:
    """
    Find intersection of two list, even if more than one element exits consider all of them
    :param l1: list
    :param l2: list
    :return: intersection list
    """
    result = []
    for x in l1:
        if x in result:
            continue
        if x in l2:
            l1_count = l1.count(x)
            l2_count = l2.count(x)
            min_count = min(l1_count, l2_count)
            result.append(x) if min_count == 1 else result.extend(([x] * min_count))
    return result


##############################################################
# endregion
