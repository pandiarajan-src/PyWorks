'''Implement Seven Segement Display for any given input integer data'''

ROWS_IN_DISPLAY = 5
COLUMNS_IN_DISPLAY = 3
DISP = {"0":[["#", "#", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"]],
        "1":[[" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"]],
        "2":[["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"]],
        "3":[["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"]],
        "4":[["#", " ", "#"], ["#", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], [" ", " ", "#"]],
        "5":[["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"]],
        "6":[["#", "#", "#"], ["#", " ", " "], ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"]],
        "7":[["#", "#", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"], [" ", " ", "#"]],
        "8":[["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"]],
        "9":[["#", "#", "#"], ["#", " ", "#"], ["#", "#", "#"], [" ", " ", "#"], ["#", "#", "#"]]}

def display_seven_segement(str_input):
    """Display seven segement display data in the console"""
    input_list = list(str_input)
    rows, columns = 0, 0
    while rows < ROWS_IN_DISPLAY:
        for str_index in input_list:
            data_to_display = DISP[str_index]
            #Reset the column count for the next number start
            columns = 0
            #It is number of spaces required between 2 digits
            print("  ", end='')
            while columns < COLUMNS_IN_DISPLAY:
                print(data_to_display[rows][columns], end='')
                columns += 1
        rows += 1
        print()


def main():
    """main method to execute the whole program"""
    try:
        int_input_data = int(input("Enter a non-negative integer number: "))
        if int_input_data < 0:
            raise ValueError
        str_input_data = str(int_input_data)
    except ValueError:
        print("Given input is not a valid value")
        main()
    else:
        display_seven_segement(str_input_data)

if __name__ == "__main__":
    main()
