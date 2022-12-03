# Context manager in Python

"""
Python came out with a special new keyword several years ago in Python 2.5 that is known as the with statement. 
This new keyword allows a developer to create context managers. 
But wait! What’s a context manager? 

They are handy constructs that allow you to set something up and tear something down automatically. 
For example, you might want to open a file, write a bunch of stuff to it and then close it. 
This is probably the classic example of a context manager. 
In fact, Python creates one automatically for you when you open a file using the with statement:
"""

with open(path, 'w') as f_obj:
    f_obj.write(some_data)


# Back in Python 2.4, you would have to do it the old fashioned way:

f_obj = open(path, 'w')
f_obj.write(some_data)
f_obj.close()

"""
The way this works under the covers is by using some of Python’s magic methods: __enter__ and __exit__. 
Let’s try creating our own context manager to demonstrate how this all works!
"""


## Creating a Context Manager class

"""
Rather than rewrite Python’s open method here, 
we’ll create a context manager that can create a SQLite database connection and close it when it’s done. 
Here’s a simple example:
"""

import sqlite3


class DataConn:
    """"""

    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """
        Open the database connection
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        self.conn.close()
        if exc_val:
            raise

if __name__ == '__main__':
    db = 'test.db'
    with DataConn(db) as conn:
        cursor = conn.cursor()

"""
In the code above, we created a class that takes a path to a SQLite database file. 
The __enter__ method executes automatically where it creates and returns the database connection object. 
Now that we have that, we can create a cursor and write to the database or query it. 
When we exit the with statement, it causes the __exit__ method to execute and that closes the connection.

Let’s try creating a context manager using another method.
"""


## Creating a Context Manager using contextlib

"""
Python 2.5 not only added the with statement, but it also added the contextlib module. 
This allows us to create a context manager using contextlib’s contextmanager function as a decorator. 
Let’s try creating a context manager that opens and closes a file after all:
"""

from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()

if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write('Testing context managers')

"""
Here we just import contextmanager from contextlib and decorate our file_open function with it. 
This allows us to call file_open using Python’s with statement. 
In our function, we open the file and then yield it out so the calling function can use it.

Once the with statement ends, control returns back to the file_open function and it continues with the code following the yield statement. 
That causes the finally statement to execute, which closes the file. 
If we happen to have an OSError while working with the file, it gets caught and finally statement still closes the file handler.
"""


### contextlib.closing(thing)

"""
The contextlib module comes with some other handy utilities. 
The first one is the closing class which will close the thing upon the completion of code block. 
The Python documentation gives an example that’s similar to the following one:
"""

from contextlib import contextmanager

@contextmanager
def closing(db):
    try:
        yield db.conn()
    finally:
        db.close()

"""
Basically what we’re doing is creating a closing function that’s wrapped in a contextmanager. 
This is the equivalent of what the closing class does. 
The difference is that instead of a decorator, we can use the closing class itself in our with statement. 
Let’s take a look:
"""

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.google.com')) as webpage:
    for line in webpage:
        # process the line
        pass

"""
In this example, we open a url page but wrap it with our closing class. 
This will cause the handle to the web page to be closed once we fall out of the with statement’s code block.
"""

## contextlib.suppress(*exceptions)

"""
Another handy little tool is the suppress class which was added in Python 3.4. 
The idea behind this context manager utility is that it can suppress any number of exceptions. 
Let’s say we want to ignore the FileNotFoundError exception. 
If you were to write the following context manager, it wouldn’t work:
"""

with open('fauxfile.txt') as fobj:
    for line in fobj:
        print(line)

#Traceback (most recent call last):
#   File "/usercode/__ed_file.py", line 1, in <module>
# with open('fauxfile.txt') as fobj:
#FileNotFoundError: [Errno 2] No such file or directory: 'fauxfile.txt''

"""
As you can see, this context manager doesn’t handle this exception. 
If you want to ignore this error, then you can do the following:
"""

from contextlib import suppress

with suppress(FileNotFoundError):
    with open('fauxfile.txt') as fobj:
        for line in fobj:
            print(line)

"""
Here we import suppress and pass it the exception that we want to ignore, which in this case is the FileNotFoundError exception. 
If you run this code, you will note that nothing happens as the file does not exist, but an error is also not raised. 
It should be noted that this context manager is reentrant. 
This will be explained later on in this section.
"""


### contextlib.redirect_stdout / redirect_stderr

"""
The contextlib library has a couple of neat tools for redirecting stdout and stderr that were added in Python 3.4 and 3.5 respectively. 
Before these tools were added, if you wanted to redirect stdout, you would do something like this:
"""

import sys

path = 'text.txt'

with open(path, 'w') as fobj:
    sys.stdout = fobj
    help(sum)

"""
With the contextlib module, you can now do the following:
"""

from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)

"""
In both of these examples, we are redirecting stdout to a file. 
When we call Python’s help, instead of printing to stdout, it gets saved directly to the file. 
You could also redirect stdout to some kind of buffer or a text control type widget from a user interface toolkit like Tkinter or wxPython.
"""

### ExitStack

"""
ExitStack is a context manager that will allow you to easily programmatically combine other context managers and cleanup functions. 
It sounds kind of confusing at first, so let’s take a look at an example from the Python documentation to help us understand this idea a bit better:
"""

from contextlib import ExitStack
with ExitStack() as stack:
    file_objects = [stack.enter_context(open(filename))
        for filename in filenames]

"""
This code basically creates a series of context managers inside the list comprehension. 
The ExitStack maintains a stack of registered callbacks that it will call in reverse order when the instance it closed, which happens when we exit the the bottom of the with statement.

There are a bunch of neat examples in the Python documentation for contextlib where you can learn about topics like the following:

Catching exceptions from __enter__ methods
Supports a variable number of context managers
Replacing any use of try-finally
and much more!

"""

