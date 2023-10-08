"""
Write a Python program to sort a list of strings based on the length of each string.
Define a custom sort function that takes a list of strings and returns a sorted list.

Example:
    Input => ["sam", "Johnathan", "Jamie", "Jeff", "Jeff", "sa", "Marina"]
    Output => ["as", "sam", "Jeff", "Jeff, "Jamie", "Marina", "Johnathan"]
"""


def sort_string_by_len_brute_force(string_list: list[str]) -> list[str]:
    temp = list()
    for item in string_list:
        temp.append([len(item), item])
    string_list.clear()
    for key, item in sorted(temp):
        string_list.append(item)
    return string_list


def sort_string_by_len_using_map(str_list_2_sort: list[str]) -> list[str]:
    return sorted(str_list_2_sort, key=len, reverse=False)
