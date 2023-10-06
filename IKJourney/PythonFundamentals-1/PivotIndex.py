# def find_pivot(numbers):
#     for index in range(len(numbers)):
#         left = numbers[:index]
#         right = numbers[index+1:]
#         if sum(left) == sum(right):
#             return index
#     return -1
# print(find_pivot([2, 3, 1, -1, 1, 1, 4]))