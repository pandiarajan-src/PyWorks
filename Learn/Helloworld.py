print("Hello it's a small world")

print("Hello " + "World " + " of a" + " Concat")

message = "hello World"
print(message.upper())
print(message.lower())
print(message.count('o'))
print(message.capitalize())

msg_list = message.capitalize().split(' ')
print(msg_list)

#input example to string
firstname = input("What is your Firstname? ")
lastname = input("What is your Lastname? ")
print("Hi " + firstname.capitalize() + ' ' + lastname.capitalize() + ' How are you doing?')
print('Hi {} {} format-1'.format(firstname, lastname))
print('Hi {1} {0} format-2'.format(lastname, firstname))

#only available on python 3
print(f'Hi  {firstname} {lastname} format-3')

