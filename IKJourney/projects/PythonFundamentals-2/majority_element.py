"""
Find the majority element in a given list.
    For a list of size n,
    the majority element is the element that appears more than floor(n/2) times.

    Example:
        Input => "nums": [3, 3, 3, 2, 2, 2, 3]
        Output => 3
            Note: 3 occurs 4 times which is greater than ⌊7/2⌋ = 3 times.

    Assumptions:
    The majority element will always exist in the input list.
    floor(x) or ⌊x⌋ denotes the floor value of any real number x.
    Floor value of any real number x is the greatest integer less than or equal to x.
"""


def find_majority_element_naive(numbers: list) -> int:
    """
    find the majority of element by counting each element and store the in a dict
    dict key holds the number and value holds the count
    :param numbers: a list containing duplicate
    :return: number that occurs maximum time in the list
    """
    num_count_dict = {}
    for num in numbers:
        if num in num_count_dict.keys():
            num_count_dict[num] += 1
        else:
            num_count_dict[num] = 1
    for key, count in num_count_dict.items():
        if count > len(numbers) // 2:
            return key


def find_majority_element_bayer_moore_method(numbers: list[int]) -> int:
    """
    To solve the problem in linear time and 0(1) space,
    Use Boyer-Moore Voting Algorithm.
    The algorithm works by maintaining a count variable and a candidate variable.
    We iterate through the array, for each element,
        we check if the count is 0, if it is, we update the candidate variable to the current element.
        We then increment the count variable if the current element is equal to the candidate,
        otherwise we decrement the count variable.
        At the end of the iteration, the candidate variable will hold the majority element.

    Complexity
    Time complexity:
    The time complexity of this algorithm is O(n), where n is the length of the array.

    Space complexity:
    The space complexity is 0(1). as we only need to maintain two variables.
    """
    majority_element = None
    count = 0
    for num in numbers:
        if count == 0:
            majority_element = num
        count += (1 if majority_element == num else -1)
    return majority_element
