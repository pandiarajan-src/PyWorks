def find_outlier(lst):
    idx = 1
    if len(lst) < 5:
        idx = 0
    else:
        actdiff = diff = lst[idx] - lst[idx-1]
        idx += 1
        while idx < len(lst):
            diff = lst[idx] - lst[idx-1]
            if diff == actdiff:
                idx += 1
                continue
            else:
                break
    idx = -1 if idx == len(lst) else idx
    return idx

list1 = [2,4,6,8,10]
print(find_outlier(list1))
list1 = [1,6,11]
print(find_outlier(list1))
list1 = [1,6,11,16,20]
print(find_outlier(list1))
list1 = [5,8,11,13,17]
print(find_outlier(list1))