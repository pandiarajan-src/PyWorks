'''my first program - hello world'''
print("Hello it's a small world")

print("Hello " + "World " + " of a" + " Concat")

MESSAGE = "hello World"
print(MESSAGE.upper())
print(MESSAGE.lower())
print(MESSAGE.count('o'))
print(MESSAGE.capitalize())

MSG_LIST = MESSAGE.capitalize().split(' ')
print(MSG_LIST)

#input example to string
FIRSTNAME = input("What is your Firstname? ")
LASTNAME = input("What is your Lastname? ")
print("Hi " + FIRSTNAME.capitalize() + ' ' + LASTNAME.capitalize() + ' How are you doing?')
print('Hi {} {} format-1'.format(FIRSTNAME, LASTNAME))
print('Hi {1} {0} format-2'.format(LASTNAME, FIRSTNAME))

#only available on python 3
print(f'Hi  {FIRSTNAME} {LASTNAME} format-3')
