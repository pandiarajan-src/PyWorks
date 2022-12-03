### Introduction to Iterators

"""
You have probably been using iterators and generators since you started programming in Python but you may not have realized it. 
In this chapter, we will learn what an iterator and a generator are. 
We will also be learning how they are created so we can create our own should we need to.

Iterators

An iterator is an object that will allow you to iterate over a container. 
The iterator in Python is implemented via two distinct methods: __iter__ and __next__. 
The __iter__ method is required for your container to provide iteration support. It will return the iterator object itself. 
But if you want to create an iterator object, then you will need to define __next__ as well, which will return the next item in the container.

To make things extra clear, let’s go over a couple of definitions:

iterable - an object that has the __iter__ method defined
iterator - an object that has both __iter__ and __next__ defined where __iter__ will return the iterator object and __next__ will return the next element in the iteration.

As with most magic methods (the methods with double-underscores), you should not call __iter__ or __next__ directly. 
Instead you can use a for loop or list comprehension and Python will call the methods for you automatically. 
There are cases when you may need to call them, but you can do so with Python’s built-ins: iter and next.

Before we move on, I want to mention Sequences. 
Python 3 has several sequence types such as list, tuple and range. The list is an iterable, 
but not an iterator because it does not implement __next__. This can be easily seen in the following example:
"""

my_list = [1, 2, 3]
next(my_list)
#Traceback (most recent call last):
#  Python Shell, prompt 2, line 1
#builtins.TypeError: 'list' object is not an iterator

"""
When we tried to call the list’s next method in the example above, 
we received a TypeError and were informed that the list object is not an iterator. But we can make it one! 
Let’s see how:
"""

print (iter(my_list))
#<list_iterator object at 0x7f6484043f28>

list_iterator = iter(my_list)
print (next(list_iterator))
#1

print (next(list_iterator))
#2

print (next(list_iterator))
#3

print (next(list_iterator))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 16, in <module>
# print (next(list_iterator))
#StopIteration:

"""
To turn the list into an iterator, just wrap it in a call to Python’s iter method. 
Then you can call next on it until the iterator runs out of items and StopIteration gets raised. 
Let’s try turning the list into an iterator and iterating over it with a loop:
"""

for item in iter(my_list):
    print(item)

#1
#2
#3

"""
When you use a loop to iterate over the iterator, you don’t need to call next and you also don’t have to worry about the StopIteration exception being raised.
"""

### Create your own iterators

"""
Creating Your Own Iterators

Occasionally you will want to create your own custom iterators. Python makes this very easy to do. 
As mentioned in the previous section, all you need to do is implement the __iter__ and __next__ methods in your class. 
Let’s create an iterator that can iterate over a string of letters:
"""

class MyIterator:

    def __init__(self, letters):
        """
        Constructor
        """
        self.letters = letters
        self.position = 0

    def __iter__(self):
        """
        Returns itself as an iterator
        """
        return self

    def __next__(self):
        """
        Returns the next letter in the sequence or 
        raises StopIteration
        """
        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.position]
        self.position += 1
        return letter

if __name__ == '__main__':
    i = MyIterator('abcd')
    for item in i:
        print(item)

"""
For this example, we only needed three methods in our class. 
In our initialization, we pass in the string of letters and create a class variable to refer to them. 
We also initialize a position variable so we always know where we’re at in the string. 
The __iter__ method just returns itself, which is all it really needs to do. 
The __next__ method is the meatiest part of this class. Here we check the position against the length of the string and raise StopIteration if we try to go past its length. 
Otherwise we extract the letter we’re on, increment the position and return the letter.

Let’s take a moment to create an infinite iterator. 
An infinite iterator is one that can iterate forever. 
You will need to be careful when calling these as they will cause an infinite loop if you don’t make sure to put a bound on them.
"""

class Doubler:
    """
    An infinite iterator
    """

    def __init__(self):
        """
        Constructor
        """
        self.number = 0

    def __iter__(self):
        """
        Returns itself as an iterator
        """
        return self

    def __next__(self):
        """
        Doubles the number each time next is called
        and returns it. 
        """
        self.number += 1
        return self.number * self.number

if __name__ == '__main__':
    doubler = Doubler()
    count = 0

    for number in doubler:
        print(number)
        if count > 5:
            break
        count += 1

"""
In this piece of code, we don’t pass anything to our iterator. We just instantiate it. 
Then to make sure we don’t end up in an infinite loop, we add a counter before we start iterating over our custom iterator. 
Finally we start iterating and break out when the counter goes above 5.
"""

### Generators

"""
A normal Python function will always return one value, whether it be a list, an integer or some other object. 
But what if you wanted to be able to call a function and have it yield a series of values? 
That is where generators come in. 
A generator works by “saving” where it last left off (or yielding) and giving the calling function a value. 
So instead of returning the execution to the caller, it just gives temporary control back. 
To do this magic, a generator function requires Python’s yield statement.

Side-note: In other languages, a generator might be called a coroutine.*

Let’s take a moment and create a simple generator!
"""

def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number

doubler = doubler_generator()
print (next(doubler))
#2

print (next(doubler))
#4

print (next(doubler))
#16

print (type(doubler))
#<class 'generator'>

"""
This particular generator will basically create an infinite sequence. 
You can call next on it all day long and it will never run out of values to yield. 
Because you can iterate over a generator, a generator is considered to be a type of iterator, but no one really refers to them as such. 
But underneath the covers, the generator is also defining the __next__ method that we looked at in our previous section, which is why the next keyword we just used worked.

Let’s look at another example that only yields 3 items instead of an infinite sequence!
"""
def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"
gen = silly_generator()
print (next(gen))
#'Python'

print (next(gen))
#'Rocks'

print (next(gen))
#'So do you!'

print (next(gen))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 15, in <module>
# print (next(gen))
#StopIteration:

"""
Here we have a generator that uses the yield statement 3 times. 
In each instance, it yields a different string. You can think of yield as the return statement for a generator. 
Whenever you call yield, the function stops and saves its state. Then it yields the value out, 
which is why you see something getting printed out to the terminal in the example above. 
If we’d had variables in our function, those variables would be saved too.

When you see StopIteration, you know that you have exhausted the iterator. 
This means that it ran out of items. 
This is normal behavior in all iterators as you saw the same thing happen in the iterators section.

Anyway when we call next again, the generator begins where it left off and yields whatever the next value is or we finish the function and the generator stops. 
On the other hand, if you never call next again, then the state will eventually go away.

Let’s reinstantiate the generator and try looping over it!
"""
gen = silly_generator()
for item in gen:
    print(item)

#Python
#Rocks
#So do you!

"""
he reason we create a new instance of the generator is that if we tried looping over it, nothing would be yielded. 
This is because we already ran through all the values in that particular instance of the generator. 
So in this example, we create the new instance, loop over it and print out the values that are yielded. 
The for loop once again handles the StopIteration exception for us and just breaks out of the loop when the generator is exhausted.

One of the biggest benefits to a generator is that it can iterate over large data sets and return them one piece at a time. 
This is what happens when we open a file and return it line-by-line:
"""
with open('file.txt') as fobj:
    for line in fobj:
        #process the line

"""
Python basically turns the file object into a generator when we iterate over it in this manner. 
This allows us to process files that are too large to load into memory. 
You will find generators useful for any large data set that you need to work with in chunks or when you need to generate a large data set that would otherwise fill up your all your computer’s memory.

"""

"""
Wrapping up
At this point you should now understand what an iterator is and how to use one. 
You should also know the difference between an iterable and an iterator. 
Finally, we learned what a generator is and why you might want to use one. 

For example, a generator is great for memory efficient data processing. 

In the next chapter, we will dig into an iterator library that is included with Python that’s called itertools.
"""