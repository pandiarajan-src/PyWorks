


def solution(input_array):
    row_size = len(input_array)
    col_size = len(input_array[0][0])
    print(f"{row_size}: {col_size}")

    array = []
    for row_content in input_array:
        for col_content in row_content:
            array.append(list(col_content))

    print(f"{array}")

    if row_size != col_size:
        return False
    a_pos = (-1, -1)
    for row in range(row_size):
        for col in range(col_size):
            if array[row][col] == 'A':
                a_pos = (row, col)
            

solution([ [".^..."], ["..X.."], ["...>X"], [".XA.."], [".<.V."] ])
