

def is_isomorphic(str_1, str_2):
    str1_lst, str1_len = list(str_1), len(str_1)
    str2_lst, str2_len = list(str_2), len(str_2)
    if str1_len != str2_len:
        return False
    charmap = {}
    used = set()
    for str1_char, str2_char in zip(str1_lst, str2_lst):
        if str1_char in charmap:
            if charmap[str1_char] != str2_char:
                return False
        else:
            if str2_char in used:
                return False
            charmap[str1_char] = str2_char
            used.add(str2_char)

    return True


if __name__ == "__main__":
    str_1 = input()
    str_2 = input()
    result = is_isomorphic(str_1, str_2)
    print('true' if result else 'false')