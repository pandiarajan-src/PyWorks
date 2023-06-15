# Pattern match
def pattern_match(str1: str, str2: str) -> bool:
    # if length of strings are not matching then false
    if len(str1) != len(str2):
        # print('not of a same length', end=' ')
        return False

    # Anagram with same size match the pattern
    if str1[::-1] == str1 and str2[::-1] == str2: 
        # print('anagram', end=' ')
        return True

    # # Find the distance between 2 characters at the same position in 2 string.
    # # if all the characters distance is same then it is same pattern
    # dist_bn_1st_pos = ord(str1[0]) - ord(str2[0])
    # dist_count = 0
    # for i in range(len(str1)):
    #     if dist_bn_1st_pos != ( ord(str1[i]) - ord(str2[i])):
    #         break
    #     dist_count += 1
    # if dist_count == len(str1):
    #     print('distance same', end= ' ')
    #     return True

    compare_str = ""
    count = 0

    for i in range(len(str1)):
        first = str1[i]
        second = str2[i]
        pos1 = compare_str.find(first)
        pos2 = compare_str.find(second)
        if pos1 == -1 and pos2 == -1:
            compare_str = compare_str + first + second
        elif pos1 > -1 and pos2 > -2 and pos2 == pos1+1:
            pass
        else:
            return False
        count += 1

    if count == len(str1):
        # print('compare logic', end= ' ')
        return True

    return False

print(f" > 1 Expected is True: {pattern_match('', '')}")
print(f" > 2 Expected is True: {pattern_match('a', 'a')}")
print(f" > 3 Expected is True: {pattern_match('x', 'y')}")
print(f" > 4 Expected is True: {pattern_match('ab', 'xy')}")
print(f" > 5 Expected is False: {pattern_match('aba', 'xyz')}")
print(f" > 6 Expected is False: {pattern_match('---', 'xyz')}")
print(f" > 7 Expected is True: {pattern_match('---', 'aaa')}")
print(f" > 8 Expected is True: {pattern_match('xyzxyz', 'toetoe')}")
print(f" > 9 Expected is False: {pattern_match('xyzxyz', 'toetoa')}")
print(f" > 10 Expected is True: {pattern_match('aaabbbcccd', 'eeefffgggz')}")
print(f" > 11 Expected is True: {pattern_match('cbacbacba', 'xyzxyzxyz')}")
print(f" > 12 Expected is True: {pattern_match('abcdefghijk', 'lmnopqrstuv')}")
print(f" > 13 Expected is False: {pattern_match('asasasasas', 'xxxxxyyyyy')}")
print(f" > 14 Expected is False: {pattern_match('ascneencsa', 'aeiouaeiou')}")
print(f" > 15 Expected is False: {pattern_match('aaasssiiii', 'gggdddfffh')}")
