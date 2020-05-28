'''Learn Functions'''
# Functions make your code more readable and easy to maintain
# To be used, when same code needs to be repeated also when same logic is needed in many places
# Always add comments to explain purpose of the functions
# In python functions must be created above it is getting called.

import datetime

def print_time():
    """Print current time"""
    print(f"{datetime.datetime.now()}")


def get_initials(name, force_upper=True):
    """Get the first character of the name in upper case
    Try to use with default value"""
    if force_upper:
        return name[0:1].upper()
    return name[0:1]


FIRST_NAME = input("Enter your first name: ")
LAST_NAME = input("Enter your last name: ")
print(f"first-name initial is {get_initials(FIRST_NAME)} \
                                and last-name initial is \
                                {get_initials(force_upper=False, name=LAST_NAME)}")
print(f"first-name initial is {get_initials(name=FIRST_NAME,force_upper=False )} \
                                and last-name initial is {get_initials(LAST_NAME)}")

print_time()

for item in range(0, 10000):
    item = item + 1

print_time()
