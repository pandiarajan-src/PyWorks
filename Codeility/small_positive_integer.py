# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(input_array):
    """ Return small positive integer in the array > 0"""
    # Implement your solution here
    input_array = sorted(input_array)
    print("", input_array)
    expected_min_value = 1
    for index_value in input_array:
        if index_value <= 0:
            continue
        else:
            print(f"{index_value} : {expected_min_value}")
            if index_value <= expected_min_value:
                expected_min_value += 1
                continue
            else:
                break
            
    print(expected_min_value)
    return expected_min_value


if __name__ == "__main__":
    solution([1, 3, 6, 4, 1, 2])

