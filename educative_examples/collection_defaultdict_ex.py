# defaultdict

# The collections module has a handy tool called defaultdict. 
# The defaultdict is a subclass of Python’s dict that accepts a default_factory as its primary argument. 
# The default_factory is usually a Python type, such as int or list, but you can also use a function or a lambda too. 
# Let’s start by creating a regular Python dictionary that counts the number of times each word is used in a sentence:

# Normal way of writing
sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

# Normal way of writing
reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1
print(reg_dict)

# Using default dict
from collections import defaultdict

def_dict = defaultdict(int)
for word in words:
    def_dict[word] += 1
print (def_dict)


# Now let’s try using a Python list type as our default factory. We’ll start off with a regular dictionary first, as before.

# Normal method
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

reg_dict = {}
for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]

print(reg_dict)

# default dict
def_dict = defaultdict(list)
for acct_num, value in my_list:
    def_dict[acct_num].append(value)
print(def_dict)


# This is some pretty cool stuff! Let’s go ahead and try using a lambda too as our default_factory!
from collections import defaultdict
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print (animal['Nick'])
#Monkey

print (animal)
#defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})

# Here we create a defaultdict that will assign ‘Monkey’ as the default value to any key. 
# The first key we set to ‘Tiger’, then the next key we don’t set at all. If you print the second key, 
# you will see that it got assigned ‘Monkey’. 
# In case you haven’t noticed yet, it’s basically impossible to cause a KeyError to happen as long as you set the default_factory to something that makes sense. 
# The documentation does mention that if you happen to set the default_factory to None, then you will receive a KeyError. 
# Let’s see how that works:

from collections import defaultdict
x = defaultdict(None)
x['Mike']
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 3, in <module>
# x['Mike']
#KeyError: 'Mike'

# In this case, we just created a very broken defaultdict. 
# It can no longer assign a default to our key, so it throws a KeyError instead. 
# Of course, since it is a subclass of dict, we can just set the key to some value and it will work. 
# But that kind of defeats the purpose of the defaultdict.

