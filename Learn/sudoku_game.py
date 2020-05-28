'''Simulate Sudoku game'''

def check_for_sudoku_success(sudo_list):
    """Check for success of SUDOKU list of list"""
    sudo_col_list = []
    for row_lst in sudo_list:
        if "".join(sorted(row_lst)) != "123456789":
            return False

    for col_index in range(0, 9):
        col_lst = [item[col_index] for item in sudo_list]
        sudo_col_list.append(col_lst)
        if "".join(sorted(col_lst)) != "123456789":
            return False

    row_index = 0
    col_index = 0
    while row_index < 9:
        col_index = 0
        while col_index < 9:
            small_sqr_list = []
            for row_internal_index in range(row_index, row_index+3):
                for col_internal_index in range(col_index, col_index+3):
                    small_sqr_list.append(sudo_list[row_internal_index][col_internal_index])
            if "".join(sorted(small_sqr_list)) != "123456789":
                return False
            col_index += 3
        row_index += 3
    return True

def get_input_value(index_pos):
    """Get input value"""
    user_input = input("Enter Sudoku's {0} row value:".format(index_pos))
    if (not user_input.isnumeric()) or (len(user_input) != 9):
        print("Plese enter correct input, it expects all digits")
        user_input = get_input_value(index_pos)
    return list(user_input)

if __name__ == "__main__":
    SUDOKU_LIST = []
    for index in range(0, 9):
        SUDOKU_LIST.append(get_input_value(index))
    if check_for_sudoku_success(SUDOKU_LIST):
        print("Given SUDOKU input is valid and you win")
    else:
        print("Given SUDOKU input is not valid and you loose")
