
##############################################################
# Simple list examples
def print_items_in_list():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num, end=" ")


# print_items_in_list()
##############################################################

##############################################################
# Print reverse of a list
def print_reverse_list(lst: list) -> list:
    lst.reverse()
    return lst


print(print_reverse_list([1, 2, 3, 4, 5]))
##############################################################


##############################################################
# Find the intersection of a two list
# The problem here is this
def print_intersection_list_naive(l1: list, l2: list) -> list:
    return [x for x in l1 if x in l2]


# print( print_intersection_list_naive([4, 2, 2, 3, 1], [2, 2, 2, 3, 3]))

def print_intersection_list_naive_fixed(l1: list, l2: list) -> list:
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


# print( print_intersection_list_naive_fixed([7, 7, 14, 92, 14, 92, 92], [0, 0, 92, 92, 7]) )
##############################################################
