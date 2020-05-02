'''Play on numbers with arthitemetic'''

def simple_math_calc():
    """Do simple mathematical calculation"""
    num_value1 = 10
    num_value2 = 20
    num_pi = 22/7
    print(num_pi)
    print('{0} + {1} = {2}'.format(num_value1, num_value2, num_value1+num_value2))
    input1 = input("Enter first number for addition? ")
    input2 = input("Enter second number for addition? ")
    print(f'String number addition {input1}, {input2}, {input1+input2}')
    print(f'number addition {input1} + {input2} = {float(input1)+float(input2)}')
    return input1, input2, num_pi, num_value1, num_value2

def is_prime(number_to_test):
    """Find whether the given number is primte"""
    for index in range(2, number_to_test-1, 1):
        if number_to_test%index == 0:
            return False
    return True

if __name__ == "__main__":
    for NUM in [3, 5, 7, 20, 17, 51, 98, 45, 67, 37, 62]:
        print("Given number {0} - Is Prime? {1}".format(NUM, is_prime(NUM)))
    #simple_math_calc()
