from colorama import init, Fore

def display(message, is_warning = False):
    if is_warning == False:
        print(Fore.BLUE + message)
    else:
        print(Fore.YELLOW + message)

display(message="This is warning message", is_warning=True)
display(message='This is correct message')

