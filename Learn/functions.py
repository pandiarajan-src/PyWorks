# Functions make your code more readable and easy to maintain
# To be used, when same code needs to be repeated also when same logic is needed in many places
# Always add comments to explain purpose of the functions
# In python functions must be created above it is getting called.

import datetime

# Prints the current time
def print_time():
    print(f"{datetime.datetime.now()}")

# Get the first character of the name in upper case 
# Try to use with default value
def get_initials(name, force_upper=True):
    if force_upper == True:
        return name[0:1].upper()
    else:
        return name[0:1]


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"first-name initial is {get_initials(first_name)} and last-name initial is {get_initials(force_upper=False, name=last_name)}")
print(f"first-name initial is {get_initials(name=first_name,force_upper=False )} and last-name initial is {get_initials(last_name)}")

print_time()

for item in range(0,10000):
    item = item + 1

print_time()