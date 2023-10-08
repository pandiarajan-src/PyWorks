"""
This file has some basic examples to try it out.
"""
import json


def call_by_reference(instr: str) -> str:
    """
    Example with Call by reference
    """
    instr = instr.upper()
    print(instr)
    return instr


g_variable = 10


def global_local_variable_test():
    """
    Global and local variable example
    :return:
    """
    global g_variable
    print(g_variable)
    g_variable = g_variable + 10
    print(g_variable)
    l_variable = 100
    print(l_variable)


def divide(x_val: int, y_val: int) -> float:
    """
    Exception handling example
    """
    result = 0.0
    try:
        result = x_val / y_val
    except ZeroDivisionError as e:
        print(e)
    finally:
        return result


def read_json_file(file_name: str):
    with open(file_name, 'r') as json_file:
        json_content = json.load(json_file)
        for key, value in json_content.items():
            print(f"{key} : {value}")


if __name__ == "__main__":
    """
    Global local variable test
    """
    # global_local_variable_test()

    """
    Call by reference example
    """
    # s1 = "panda"
    # print(s1)
    # call_by_reference(s1)
    # print(s1)

    """
    Divide exception handling
    """
    # user_input = tuple(input("Enter two numbers with space to find division:").split())
    # x, y = int(user_input[0]), int(user_input[1])
    # print(divide(x, y))

    """
    Read JSON example
    """
    read_json_file("english_json.json")