"""
Write a Python program to sort a list of strings based on the length of each string.
Define a custom sort function that takes a list of strings and returns a sorted list.
"""


def sort_string_by_len(string_list: list) -> list:
    temp = list()
    for item in string_list:
        temp.append([len(item), item])
    string_list.clear()
    for key, item in sorted(temp):
        string_list.append(item)
    return string_list


print(sort_string_by_len(["there", "hi", "test", "hello", "how", "are"]))
print(sorted(["there", "hi", "test", "hello", "how", "are"]))
