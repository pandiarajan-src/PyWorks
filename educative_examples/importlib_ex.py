# importlib

"""
Python provides the importlib package as part of its standard library of modules. 
Its purpose is to provide the implementation to Python’s import statement (and the __import__() function). 
In addition, importlib gives the programmer the ability to create their own custom objects (AKA an importer) that can be used in the import process.

What about imp?

There is another module called imp that provides an interface to the mechanisms behind Python’s import statement. 
This module was deprecated in Python 3.4. It is intended that importlib should be used in its place.

This module is pretty complicated, so we’ll be limiting the scope of this chapter to the following topics:

Dynamic imports
Checking if a module can be imported
Importing from the source file itself
A clever 3rd party module called import_from_github_com

"""

# Dynamic imports

"""
The importlib module supports the ability to import a module that is passed to it as a string. 
So let’s create a couple of simple modules that we can work with. 
We will give both modules the same interface, but have them print their names so we can tell the difference between the two. 
Create two modules with different names such as foo.py and bar.py and add the following code in each of them:
"""
def main():
    print(__name__)

"""
Now we just need to use importlib to import them. Let’s look at some code to do just that. 
Make sure that you put this code in the same folder as the two modules you created above.
"""

 # importer.py}
import importlib
import foo


def dynamic_import(module):

    return importlib.import_module(module)


if __name__ == '__main__':
    module = dynamic_import('foo')
    module.main()

    module_two = dynamic_import('bar')
    module_two.main()

"""
Here we import the handy importlib module and create a really simple function called dynamic_import. 
All this function does is call importlib’s import_module function with the module string that we passed in and returns the result of that call. 
Then in our conditional statement at the bottom, we call each module’s main method, which will dutifully print out the name of the module.

You probably won’t be doing this a lot in your own code, but occasionally you’ll find yourself wanting to import a module when you only have the module as a string. 
The importlib module gives us the ability to do just that.
"""

### Module import check

"""
Python has a coding style that is known as EAFP: Easier to ask for forgiveness than permission. 
What this means is that it’s often easier to just assume that something exists (like a key in a dict) and catch an exception if we’re wrong. 
You saw this in our previous chapter where we would attempt to import a module and we caught the ImportError if it didn’t exist. 
What if we wanted to check and see if a module could be imported rather than just guessing? You can do that with importlib! 
Let’s take a look:
"""

import importlib.util

def check_module(module_name):
    """
    Checks if module can be imported without actually
    importing it
    """
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module: {} not found'.format(module_name))
        return None
    else:
        print('Module: {} can be imported!'.format(module_name))
        return module_spec


def import_module_from_spec(module_spec):
    """
    Import the module via the passed in module specification
    Returns the newly imported module
    """
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module

if __name__ == '__main__':
    module_spec = check_module('fake_module')
    module_spec = check_module('collections')
    if module_spec:
        module = import_module_from_spec(module_spec)
        print(dir(module))

"""
Here we import a submodule of importlib called util. The check_module code has the first piece of magic that we want to look at.
In it we call the find_spec function against the module string that we passed in. 
First we pass in a fake name and then we pass in a real name of a Python module. 
If you run this code, you will see that when you pass in a module name that is not installed, 
the find_spec function will return None and our code will print out that the module was not found. 
If it was found, then we will return the module specification.

We can take that module specification and use it to actually import the module. 
Or you could just pass the string to the import_module function that we learned about in the previous section. 
But we already covered that so let’s learn how to use the module specification. 
Take a look at the import_module_from_spec function in the code above. 
It accepts the module specification that was returned by check_module. 
We then pass that into importlib’s module_from_spec function, which returns the import module. 
Python’s documentation recommends executing the module after importing it, so that’s what we do next with the exec_module function. 
Finally we return the module and run Python’s dir against it to make sure it’s the module we expect.
"""

### Import from source file

"""
The importlib’s util sub-module has another neat trick that I want to cover. 
You can use util to import a module using just its name and file path. 
The following is a very derived example, but I think it will get the point across:
"""

import importlib.util

def import_source(module_name):
    module_file_path = module_name.__file__
    module_name = module_name.__name__

    module_spec = importlib.util.spec_from_file_location(
        module_name, module_file_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    print(dir(module))

    msg = 'The {module_name} module has the following methods:' \
        ' {methods}'
    print(msg.format(module_name=module_name, 
                     methods=dir(module)))

if __name__ == '__main__':
    import logging
    import_source(logging)

"""
In the code above, we actually import the logging module and pass it to our import_source function. 
Once there, we grab the module’s actual path and its name. 
Then we call pass those pieces of information into the util’s spec_from_file_location function which will return the module’s specification. 
Once we have that, we can use the same importlib mechanisms that we used in the previous section to actually import the module.

Now let’s look at a neat 3rd party module that Python’s __import__() function to import packages directly from github!
"""

### Import from github.com

"""
import_from_github_com
There’s a neat package called import_from_github_com that can be used to find and load modules from github. 
To install it, all you need to do is use pip like this:

pip install import_from_github_com

The package uses the new import hooks provided in PEP 302 to basically allow you to import a package from github. 
What the package actually appears to do is install the package and add it to locals. 
Regardless, you will need Python 3.2 or greater, git and pip to use this package.

Once those are installed, you can try doing this in your Python shell:
"""

from github_com.zzzeek import sqlalchemy
#Collecting git+https://github.com/zzzeek/sqlalchemy
#  Cloning https://github.com/zzzeek/sqlalchemy to /tmp/pip-acfv7t06-build
#Installing collected packages: SQLAlchemy
#  Running setup.py install for SQLAlchemy ... done
#Successfully installed SQLAlchemy-1.1.0b1.dev0

print(locals())
#{'sqlalchemy': <module 'sqlalchemy' from '/usr/local/lib/python3.5/dist-packages/sqlalchemy/__init__.py'>,
#'__file__': '/usercode/__ed_file.py', '__package__': None, '__cached__': None, '__doc__': None,
#'__spec__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7fd93d1775c0>,
#'__name__': '__main__', '__builtins__': <module 'builtins' (built-in)>}

"""
If you take a look at the source code for import_from_github_com, you will notice that it isn’t using importlib. 
Instead it uses pip to install the package if it’s not installed and then it uses Python’s __import__() function to actually import the newly installed module. 
It’s a really clever piece of code that is well worth studying.
"""

"""
Wrapping up!!!
At this point, you should have an idea of how you might use importlib and import hooks in your own code. 
There is a lot more to this module than what is covered in this chapter, 
so if you have a need to write a custom importer or loader then you’ll want to spend some time reading the documentation and the source code.
"""