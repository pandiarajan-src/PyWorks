'''Simulate TIC-TAC-TOE game, no intelligence mostly user wins'''

from random import randrange
from math import trunc, modf

def calculate_row_column(value, matrix_size):
    """Find matrix row and column position of a given number"""
    column_value = round(1/matrix_size-.01, 1)
    column, row = modf(value/matrix_size-0.01)
    column, row = trunc(column/column_value)-1, trunc(row)
    return (row, column)

def verify_board_size(board):
    """Verify whether the given board size is correct, both column and row should be equal"""
    row_max_size = len(board)
    if row_max_size <= 0:
        return (0, 0)
    col_max_size = len(board[0])
    if col_max_size <= 0:
        return (0, 0)
    if row_max_size != col_max_size:
        print("It is expected that both row size and column size should be same")
        return (0, 0)
    return (row_max_size, col_max_size)

def display_board(board):
    """the function accepts one parameter containing the board's current status\
    and prints it out to the console"""

    row_max_size, col_max_size = verify_board_size(board)
    if row_max_size == 0 or col_max_size == 0:
        return
    for row in range(row_max_size):
        print("{0}+".format(row_max_size*"+-------"))
        for draw_column in range(3):
            if draw_column == 1:
                for column in range(col_max_size):
                    print("|   {0}   ".format(board[row][column]), end="")
                print("|")
            else:
                print("{0}|".format(col_max_size*"|       "))
    print("{0}+".format(row_max_size*"+-------"))

def enter_user_move(board):
    """the function accepts the board current status, asks the user about their move, \
    checks the input and updates the board according to the user's decision"""

    row_max_size, col_max_size = verify_board_size(board)
    if row_max_size == 0 or col_max_size == 0:
        return
    value = 0
    available_pos = get_list_of_free_fields(board)
    while True:
        try:
            value = int(input("\n Enter your move: "))
            if (value > 0) or (value <= 9):
                break
            if value not in available_pos:
                raise AttributeError
        except ValueError:
            print("Invalid entry, please enter number between 0 to 9")
        except AttributeError:
            print("The position is not avaialble, please enter different position")
    row, column = calculate_row_column(value, row_max_size)
    board[row][column] = "o"
    #Display board entry once computer entry is made
    display_board(board)



def get_list_of_free_fields(board):
    """the function browses the board and builds a list of all the free squares;\
    the list consists of tuples, while each tuple is a pair of row and column numbers
    """
    available_pos_list = []
    for row_list in board:
        for column_number in row_list:
            if str(column_number).isdigit():
                available_pos_list.append(column_number)
    return available_pos_list


def check_for_victory(board):
    """
    the function analyzes the board status in order to check if
    the player using 'O's or 'X's has won the game
    """
    row_len = len(board)
    col_len = len(board[0])
    #Row check
    for row_list in board:
        result = len(row_list) > 0 and all(elem == row_list[0] for elem in row_list)
        if result:
            return (True, row_list[0])

    #Column check
    for col_index in range(col_len):
        column_lst = []
        column_lst.clear()
        for row_index in range(row_len):
            column_lst.append(board[row_index][col_index])
        result = len(column_lst) > 0 and all(elem == column_lst[0] for elem in column_lst)
        if result:
            return (True, column_lst[0])

    #Diagonal check from top-left to bottom right
    diag_lst = []
    for diag_index in range(row_len):
        diag_lst.append(board[diag_index][diag_index])
    result = len(diag_lst) > 0 and all(elem == diag_lst[0] for elem in diag_lst)
    if result:
        return (True, diag_lst[0])

    diag_lst.clear()
    #Diagonal check from bottom-left to top-right
    min_val, max_val = 0, col_len-1
    while min_val < col_len-1:
        diag_lst.append(board[min_val][max_val])
        min_val += 1
        max_val -= 1
    result = len(diag_lst) > 0 and all(elem == diag_lst[0] for elem in diag_lst)
    if result:
        return (True, diag_lst[0])

    #no one success yet
    return (False, " ")


def enter_computer_move(board):
    """the function draws the computer's move and updates the board"""
    value = 0
    avail_pos_list = get_list_of_free_fields(board)
    while True:
        value = randrange(1, 9, 1)
        if value in avail_pos_list:
            break
    row, column = calculate_row_column(value, len(board))
    board[row][column] = "x"
    #Display board entry once computer entry is made
    display_board(board)

if __name__ == "__main__":
    BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    display_board(BOARD)
    INDEX = 0
    print("**************Start of Game*****************")
    while True:
        enter_computer_move(BOARD)
        enter_user_move(BOARD)
        INDEX += 1
        if INDEX >= len(BOARD)-1:
            STATUS, SIGN = check_for_victory(BOARD)
            if STATUS and SIGN == "x":
                print("***Computer Wins***")
                break
            if STATUS and SIGN == "o":
                print("****User Wins***")
                break
            if len(get_list_of_free_fields(BOARD)) <= 0:
                print("***No Wins, its TIE***")
                break
    print("**************End of Game*****************")
