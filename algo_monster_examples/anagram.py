
from typing import List
import collections

def group_anagrams(strs : List[str]) -> List[List[str]]:
    ana_grp = {}
    for str in strs:
        ordered_str = "".join(sorted(str))
        if ordered_str in ana_grp:
            ana_grp[ordered_str].append(str)
        else:
            ana_grp[ordered_str] = [str]
    return list(ana_grp.values())
        

if __name__ == "__main__":
    strs = input().split()
    result = group_anagrams(strs)
    for list_val in result:
        list_val.sort()
    result.sort(key=lambda row: row[0])
    for list_val in result:
        print(" ".join(list_val))

    
