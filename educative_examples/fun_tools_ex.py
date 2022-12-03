# functools

"""
Python comes with a fun module called functools. 
The functions inside functools are considered “higher-order” functions which can act on or return other functions. 
In this chapter we will be looking at the following portions of the functools package:

lru_cache
partials
singledispatch
wraps

Let’s get started by learning how to create a simple cache with Python!
"""

"""
Caching with functools.lru_cache

The functools module provides a handy decorator called lru_cache. 
Note that it was added in Python 3.2. According to the documentation, it will “wrap a function with a memoizing callable that saves up to the maxsize most recent calls”. 
In other words, it’s a decorator that adds caching to the function it decorates. 
Let’s write a quick function based on the example from the functools documentation that will grab various web pages. 
In this case, we’ll be grabbing pages from the Python documentation site.
"""

import urllib.error
import urllib.request

from functools import lru_cache


@lru_cache(maxsize=24)
def get_webpage(module):
    """
    Gets the specified Python module web page
    """    
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None

if __name__ == '__main__':
    modules = ['functools', 'collections', 'os', 'sys']
    for module in modules:
        page = get_webpage(module)
        if page:
            print("{} module page found".format(module))


"""
In the code above, we decorate our get_webpage function with lru_cache and set its max size to 24 calls. 
Then we set up a webpage string variable and pass in which module we want our function to fetch. 
I found that this works best if you run it in a Python interpreter, such as IDLE. 
This allows you to run the loop a couple of times against the function. What you will quickly see is that the first time it runs the code, the output is printed our relatively slowly. 
But if you run it again in the same session, you will see that it prints immediately which demonstrates that the lru_cache has cached the calls correctly. Give this a try in your own interpreter instance to see the results for yourself.

There is also a typed parameter that we can pass to the decorator. 
It is a Boolean that tells the decorator to cache arguments of different types separately if typed is set to True.
"""

### functool.partial

"""
One of the functools classes is the partial class. 
You can use it create a new function with partial application of the arguments and keywords that you pass to it. 
You can use partial to “freeze” a portion of your function’s arguments and/or keywords which results in a new object. 
Another way to put it is that partial creates a new function with some defaults. 
Let’s look at an example!
"""

from functools import partial
def add(x, y):
    return x + y

p_add = partial(add, 2)
print(p_add(4))
#6

"""
Here we create a simple adding function that returns the result of adding its arguments, x and y. 
Next we create a new callable by creating an instance of partial and passing it our function and an argument for that function. 
In other words, we are basically defaulting the x parameter of our add function to the number 2. 
Finally we call our new callable, p_add, with the argument of the number 4 which results in 6 because 2 + 4 = 6.
"""

"""
here’s a really basic example of passing a partial function around:
"""
from functools import partial


def add(x, y):
    """"""
    return x + y


def multiply(x, y):
    """"""
    return x * y


def run(func):
    """"""
    print(func())


def main():
    """"""
    a1 = partial(add, 1, 2)
    m1 = partial(multiply, 5, 8)
    run(a1)
    run(m1)

if __name__ == "__main__":
    main()

"""
Here we create a couple of partial functions in our main function. 
Next we pass those partials to our run function, call it and then print out the result of the function that was called.
"""

### Function Overloading with functools.singledispatch

"""
Python fairly recently added partial support for function overloading in Python 3.4. 
They did this by adding a neat little decorator to the functools module called singledispatch. 
This decorator will transform your regular function into a single dispatch generic function. 
Note however that singledispatch only happens based on the first argument’s type. 
Let’s take a look at an example to see how this works!
"""
from functools import singledispatch


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    add(1, 2)
    add('Python', 'Programming')
    add([1, 2, 3], [5, 6, 7])

"""
Here we import singledispatch from functools and apply it to a simple function that we call add. 
This function is our catch-all function and will only get called if none of the other decorated functions handle the type passed. 
You will note that we currently handle integers, strings and lists as the first argument. 
If we were to call our add function with something else, such as a dictionary, then it would raise a NotImplementedError.

Try running the code yourself. You should see output that looks like this:

As you can see, the code works exactly as advertised. 
It calls the appropriate function based on the first argument’s type. 
If the type isn’t handled, then we raise a NotImplementedError. 
If you want to know what types we are currently handling, you can add the following piece of code to the end of the file, preferable before the line that raises an error:
"""

print(add.registry.keys())

"""
This will print out something like this:
dict_keys([<class 'str'>, <class 'int'>, <class 'list'>, <class 'object'>])
"""

"""
This tells us that we can handle strings, integers, lists and objects (the default). 
The singledispatch decorator also supports decorator stacking. 
This allows us to create an overloaded function that can handle multiple types. 
Let’s take a look:
"""

from functools import singledispatch
from decimal import Decimal


@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')


@add.register(float)
@add.register(Decimal)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    add(1.23, 5.5)
    add(Decimal(100.5), Decimal(10.789))

"""
This basically tells Python that one of the add function overloads can handle float and decimal.Decimal types as the first argument. 
If you run this code, you should see something like the following:

First argument is of type  <class 'float'>
6.73
First argument is of type  <class 'decimal.Decimal'>
111.2889999999999997015720510
dict_keys([<class 'float'>, <class 'int'>, <class 'object'>, <class 'decimal.Decimal'>

"""


### functools.wraps

"""
There is a little known tool that I wanted to cover in this section. 
It is called wraps and it too is a part of the functools module. You can use wraps as a decorator to fix docstrings and names of decorated functions. 
Why does this matter? 
This sounds like a weird edge case at first, but if you’re writing an API or any code that someone other than yourself will be using, then this could be important. 
The reason being that when you use Python’s introspection to figure out someone else’s code, a decorated function will return the wrong information. 
Let’s look at a simple example that I have dubbed decorum.py:
"""

# decorum.py


def another_function(func):
    """
    A function that accepts another function
    """

    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper


@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)

"""
The output will be
wrapper

        A wrapping function
"""

"""
That’s not right! If you run this program in IDLE or the interpreter, 
it becomes even more obvious how this can get really confusing, really quickly.
"""

mport decorum

help(decorum)
#Help on module decorum:

#NAME
#    decorum - 

#FILE
#    /home/mike/decorum.py

#FUNCTIONS
#    a_function = wrapper()
#        A wrapping function

#    another_function(func)
#        A function that accepts another function

help(decorum.a_function)
#Help on function other_func in module decorum:

#wrapper()
#    A wrapping function

"""
Basically what is happening here is that the decorator is changing the decorated function’s name and docstring to its own.
"""

"""
How do we fix this little mess? The Python developers have given us the solution in functools.wraps! Let’s check it out:

"""

def another_function(func):
    """
    A function that accepts another function
    """

    @wraps(func)
    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper


@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    #a_function()
    print(a_function.__name__)
    print(a_function.__doc__)

"""
Here we import wraps from the functools module and use it as a decorator for the nested wrapper function inside of another_function. 
If you run it this time, the output will have changed:

The output will be
a_function
A pretty useless function

"""

### Wrappig up

"""
Let’s review. In this chapter, you learned some basic caching using lru_cache. 
Then we moved onto partials which lets you “freeze” a portion of your function’s arguments and/or keywords allowing you to create a new object that you can call. 
Next we used singledispatch to overload functions with Python. While it only allows function overloading based on the first argument, this is still a handy tool to add to your arsenal! 
Finally we looked at wraps which had a very narrow focus: namely it fixes docstrings and function names that have been decorated such that they don’t have the decorator’s docstring or name any more.
"""