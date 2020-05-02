'''input integer values and check if they are within a specified range'''

def read_input(prompt, min_val, max_val):
    """read the input values and check the min & max range"""
    try:
        int_data = int(input("Enter a number between {0} & {1} : ".format(min_val, max_val)))
        if int_data not in range(min_val, max_val+1, 1):
            raise LookupError
    except LookupError:
        print("Error: value {0} is not within range ({1}..{2})".format(int_data, min_val, max_val))
        int_data = read_input(prompt, min_val, max_val)
    except ValueError:
        print("Error: wrong input")
        int_data = read_input(prompt, min_val, max_val)
    else:
        return int_data

def main():
    """Execute the main method code here"""
    input_data = read_input("Enter the number from -10 to 10: ", -10, 10)
    print("input number {0} is within the range({1}, {2})".format(input_data, -10, 10))

if __name__ == "__main__":
    main()
