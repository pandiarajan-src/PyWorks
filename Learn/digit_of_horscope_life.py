'''Digit of horscope of life'''

def calculate_digit_of_life(input_data):
    """Calculate digit of life, its yours horscope value"""
    if not input_data.isnumeric():
        print("given input is not valid")
    value = 0
    for index in input_data:
        value += int(index)
    if value > 9:
        value = calculate_digit_of_life(str(value))
    return value

if __name__ == "__main__":
    USER_INPUT = input("Enter your DOB as YYYYMMDD (all digits)")
    print("Digit of your life: {0}".format(calculate_digit_of_life(USER_INPUT)))
