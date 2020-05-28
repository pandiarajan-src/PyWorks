'''Learn collections by examples'''
from array import array
#from datetime import datetime

# Play with list
# It can contain any items of any type, (Store anything, Store any type)
# Zero based index and Storage order is guaranteed
INT_LIST = [4, 20.34, 3, 1, 10.12]
STR_LIST = ['all', 'tat', 'are', 'good', 'test', 0, 1, 1.23]
INT_LIST.append(5)
STR_LIST.insert(0, 'hi')
print("Size of int_list is {0} and its contents are {1}".format(INT_LIST.__len__(), INT_LIST))
INT_LIST.sort()
print("Sorted list is {0}".format(INT_LIST))
print("Size of str_list is {0} and its contents are {1}".format(STR_LIST.__len__(), STR_LIST))
print("First Index element in int_list: {0}".format(INT_LIST[0]))
print("Last index element in str_list: {0}".format(STR_LIST[(STR_LIST.__len__() - 1)]))
print(f"First two element in str_list: {STR_LIST[0:2]}")
print("*************************************************************")

# Play with Lists
# Must be all simple types and all the items in the list of same type.
# Zero based index and Storage order is guaranteed
INT_ARRAY = array('d')
INT_ARRAY.append(11)
INT_ARRAY.append(22.22)
INT_ARRAY.insert(0, 2)
print("Size of int_array is {0} and its contents are {1}".format(INT_ARRAY.__len__(), INT_ARRAY))
print("First index element in int_array: {0}".format(INT_ARRAY[0]))

# Play with Dictionary
# Stores Key value pairs,
# Storage order is not guaranteed.
MONTHLY_SENSEX_START = {'01-01-2019': 37100, '01-02-2019': 37200}
MONTHLY_SENSEX_START['01-04-2019'] = 37400
print(f'Montly sensex start dictionary values: {MONTHLY_SENSEX_START}')
print('Start of the year sensex value: {0}'.format(MONTHLY_SENSEX_START['01-01-2019']))

# Play with both List and Dictionary
BILL = {'first': 'Bill', 'Last': 'Gates', 'DOB': '01-01-2019'}
JOBS = {'first': 'Steve', 'Last': 'Jobs', 'DOB': '01-01-2019'}

FAMOUS_PEOPLE = [BILL, JOBS]
print(f'My famous people lists are {len(FAMOUS_PEOPLE)} : {FAMOUS_PEOPLE}')
