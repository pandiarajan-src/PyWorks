'''Learn loops'''
# Python has only 2 loops 1. For 2. While
# For - To be used when you want to run for specific times based on collection
# index etc (mostly and always for collections)
# While - To be used when something automatically change a condition inside while
# (e.g: reading lines in file etc)

for item in ['hi', 'how', 'are', 'you', 99, 88]:
    print(item)

for item in range(0, 10):
    print(item)

INDEX = 0
while INDEX < 10:
    print(INDEX*11)
    INDEX = INDEX + 1
