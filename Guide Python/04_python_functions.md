Python
=========================
Updated: 18/04/2020
[Return to Index](./00_python_index.md)

# Table of contents

1. [Introduction](#introduction)
2. [Functions](#functions)\
2.1. [Function Definition](#function-definition)\
2.2. [Default Parameter Values](#default-parameter-values)\
2.3. [Variadic Arguments](#variadic-arguments)
3. [Anonymous Functions](#anonymous-functions)
4. [Modules and Import](#modules-and-import)

# Python Functions

## Introduction

In python we can wrap our instructions inside **functions** that usually describe one functionality. These functions can be called afterwards as many times as wanted.

We have already seen **built-in** functions that are provided by the language such as ``range()`` or ``print()``. We will learn in this chapter how to make **user-defined** functions.

## Functions

### Function definition

The basic syntax of a function is:

```python
def my_function(args_list):
	"""Documentation"""
	# do something
```

You may (or may not) give arguments to the function, depending on the functionality. A python function can also return some sort of value.

```python
def print_hello_world():
	print("Hello World!")


def increment(arg1):
	return arg1 += 1
```

A function in Python can also return multiple values, in the form of a **tuple** (see [Python Structures](./python_structures.md)).

```python
def increment_all(arg1, arg2):
	arg1 += 1
	arg2 += 1
	return arg1, arg2


arg1 = 1
arg2 = 3

print(increase_all(arg1, arg2)) # (2, 4)
```

### Default Parameter Values

When defining a function, we may need to add parameters that will be given when the function is called, as seen above. Some of these arguments may have a default value and not require the argument when the function is called.

```python
def merry_christmas(name, message = 'I wish you a Merry Christmas'):
	print("Hello " + name + ", " + message)

merry_christmas("Bobby")                 # Hello Bobby, I wish you a Merry Christmas
merry_christmas("Karen", "I hate you")   # Hello Karen, I hate you
```

The arguments can be given unordered if the names of the parameters are specified.

### Variadic Arguments

When defining a function, we can choose how many parameters we will need to give when calling the function, as seen above. We don't need to know in advance how many parameters we can pass to the function, as we have the ``*args`` and ``*kwargs`` constructions to do so.

* ``*args``

Allows several parameters to be passed to the function. We will be able to iterate through those elements with a ``for`` loop.

```python
def function(*args):
    for arg in args:
        # do something with each argument

function("e1", "e2", "e3", ...)
```

* ``**kwargs``

Almost the same as the option above, but each element is associated to a **key**.

```python
def function(**kwargs):
    for arg in kwargs.values():
        # do something with each argument

function(a="e1", b="e2", c="e3", ...)
```

## Anonymous Functions

When we want to create a function and use it once, or we are able to keep it in a data structure, we may want to create a nameless function. These are defined using the keyword ``lambda`` and the general syntax is:

```python
lambda arguments: expression
```

The expression must be a single instructions. However, we can pass as many arguments as we want, considering that the expression won't allow iterations.

```python
increment = lambda value: value + 1
add = lambda first, second: first + second

print(increment(0))   # 1
print(add(1, 2))      # 3
```

## Modules and Import

Modules allow the developer to group related functions, classes and code in a library or a single file. This allows the code to be organized so that it can be maintained and be easily read.

We can use the keyword ``import`` in our file in order to use code from another module, such as functions or attributes. We can also use the statement ``from <module> import <code>`` to use the code without having to write the name of the module each time.

```python
import labyrinth

labyrinth.function1()
labyrinth.function2()

from labyrinth import *

function1()
function2()
```

By convention, imports are done at the top of the file.