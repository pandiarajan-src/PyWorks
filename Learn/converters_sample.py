'''This example script shows how to convert different units - excercise for variables'''

MILES_TO_KILO_CONST = 1.609344
RESOLUTION_CONST = 2

def miles_to_kilometers(miles):
    """Convert given input miles to kilometers"""
    return round((miles * MILES_TO_KILO_CONST), RESOLUTION_CONST)

def kilometers_to_miles(kilometers):
    """Convert given inputs kilometers to miles"""
    return round((kilometers/MILES_TO_KILO_CONST), RESOLUTION_CONST)

def main():
    """main method to execute the complete code"""
    try:
        input_data = int(input("Enter input for miles to kilo and vice-versa : "))
        print("Input: {0} Miles to Kilometers : {1}".format(input_data, \
                                                            miles_to_kilometers(input_data)))
        print("Input: {0} Kilometers to Miles : {1}".format(input_data, \
                                                            kilometers_to_miles(input_data)))
    except Exception as e_catch: # pylint: disable=broad-except
        print("Exception message {0}".format(e_catch.__str__))


if __name__ == "__main__":
    main()
