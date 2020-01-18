from array import array
from datetime import datetime

# Play with list
# It can contain any items of any type, (Store anything, Store any type)
# Zero based index and Storage order is guaranteed
int_list = [4, 20.34, 3, 1, 10.12]
str_list = ['all', 'tat', 'are', 'good', 'test', 0, 1, 1.23]
int_list.append(5)
str_list.insert(0, 'hi')
print("Size of int_list is {0} and its contents are {1}".format(int_list.__len__(), int_list))
int_list.sort()
print("Sorted list is {0}".format(int_list))
print("Size of str_list is {0} and its contents are {1}".format(str_list.__len__(), str_list))
print("First Index element in int_list: {0}".format(int_list[0]))
print("Last index element in str_list: {0}".format(str_list[(str_list.__len__() - 1)]))
print(f"First two element in str_list: {str_list[0:2]}")
print("*************************************************************")

# Play with Lists
# Must be all simple types and all the items in the list of same type.
# Zero based index and Storage order is guaranteed
int_array = array('d')
int_array.append(11)
int_array.append(22.22)
int_array.insert(0, 2)
print("Size of int_array is {0} and its contents are {1}".format(int_array.__len__(), int_array))
print("First index element in int_array: {0}".format(int_array[0]))

# Play with Dictionary
# Stores Key value pairs, 
# Storage order is not guaranteed.
monthly_sensex_start = {'01-01-2019': 37100, '01-02-2019': 37200}
monthly_sensex_start['01-04-2019'] = 37400
print(f'Montly sensex start dictionary values: {monthly_sensex_start}' )
print('Start of the year sensex value: {0}'.format(monthly_sensex_start['01-01-2019']))

# Play with both List and Dictionary
bill = {'first': 'Bill', 'Last': 'Gates', 'DOB': '01-01-2019'}
jobs = {'first': 'Steve', 'Last': 'Jobs', 'DOB': '01-01-2019'}

famous_people = [bill, jobs]
print(f'My famous people lists are {len(famous_people)} : {famous_people}')

