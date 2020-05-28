'''Learn import modules'''
# Import functions module as namespace
import functions
from functions import print_time
functions.print_time()

# Import only specific items into current namespace

print_time()

# Import all items into current namespace
#from functions import *
print_time()

# during the import if you have anything non functions or class global statement
# the global statements also will be executed when you export the whole import

# Packages are collection of modules
# Use pip install command (use txt file for list of packages)
