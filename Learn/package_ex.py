'''Learn packages'''
from colorama import Fore #,init

def display(message, is_warning=False):
    """Print message in different color in console"""
    if not is_warning:
        print(Fore.BLUE + message)
    else:
        print(Fore.YELLOW + message)

display(message="This is warning message", is_warning=True)
display(message='This is correct message')
