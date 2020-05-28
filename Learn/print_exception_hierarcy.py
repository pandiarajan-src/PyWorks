'''Learn to print python exceptions in console as hierarcy tree'''

def print_python_exception_tree(thisclass, nest=0):
    """Print python exception tree in console as tree"""
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_python_exception_tree(subclass, nest + 1)

print_python_exception_tree(BaseException)
