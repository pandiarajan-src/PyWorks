from turtle import left, right
from typing import List


def basic_sort(unsorted_list : List[int]) -> List[int]:
    for i in range(len(unsorted_list)):
        for j in range(i, len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[j], unsorted_list[i] = unsorted_list[i], unsorted_list[j]

    return unsorted_list


def insertion_sort(unsorted_list : List[int]) -> List[int]:
    for i, entry in enumerate(unsorted_list):
        current = i
        while current > 0 and unsorted_list[current-1] > unsorted_list[current]:
            unsorted_list[current-1], unsorted_list[current] = unsorted_list[current], unsorted_list[current-1]
            current -= 1

    return unsorted_list

def selection_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    
    return unsorted_list

def bubble_sort(unsorted_list : List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        swapped = False
        for j in range(i, n):
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[j], unsorted_list[i] = unsorted_list[i], unsorted_list[j]
                swapped = True
        if not swapped:
            return unsorted_list

    return unsorted_list

def merge_sort_step2(left_list : List[int], right_list : List[int]) -> List[int]:
    left_pointer, right_pointer = 0, 0
    result_list = []
    l_n = len(left_list)
    r_n = len(right_list)
    while left_pointer < l_n and right_pointer < r_n:        
        if(left_list[left_pointer] <= right_list[right_pointer]):
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
    if(left_pointer < l_n):
        result_list.extend(left_list[left_pointer:])
    elif(right_pointer < r_n):
        result_list.extend(right_list[right_pointer:])
    
    return result_list

def merge_sort_step1(unsorted_list : List[int]) -> List[int]:
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    
    mid_point = n // 2
    left_list, right_list = merge_sort_step1(unsorted_list[:mid_point]), merge_sort_step1(unsorted_list[mid_point:])
    result_list = merge_sort_step2(left_list, right_list)
    return result_list
        
def merge_sort(unsorted_list : List[int]) -> List[int]:
    return merge_sort_step1(unsorted_list)

def quick_sort_recursive(unsorted_list : List[int], start : int, end : int ) -> None:
    if (end - start) <= 1:
        return None
    pivot = unsorted_list[end-1]
    start_pointer = start
    end_pointer = end -1
    while start_pointer < end_pointer:
        while unsorted_list[start_pointer] < pivot and start_pointer < end_pointer:
            start_pointer += 1
        while unsorted_list[end_pointer] >= pivot and start_pointer < end_pointer:
            end_pointer -= 1
        if start_pointer == end_pointer:
            break
        unsorted_list[start_pointer], unsorted_list[end_pointer] = unsorted_list[end_pointer], unsorted_list[start_pointer]
    
    unsorted_list[start_pointer], unsorted_list[end-1] = unsorted_list[end-1], unsorted_list[start_pointer]
    quick_sort_recursive(unsorted_list, start, start_pointer)
    quick_sort_recursive(unsorted_list, start_pointer+1, end)
    


def quick_sort(unsorted_list : List[int]) -> List[int]:
    quick_sort_recursive(unsorted_list, 0, len(unsorted_list))
    return unsorted_list


if __name__ == "__main__":
    unsorted_lst = [int(x) for x in input().split()]
    sorted_list = quick_sort(unsorted_lst)
    print(' '.join(map(str, sorted_list)))