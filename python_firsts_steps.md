Python
=========================
Updated: 18/04/2020

# Table of contents

1. [Introduction](#introduction)
2. [Setup](#setup)\
2.1. [Download Python](#download-python)\
2.2. [PyCharm IDE](#pycharm-ide)\
2.3. [Executing python scripts outside the IDE](#executing-python-scripts-outside-the-ide)
3. [Programming with Python](#programming-with-python)\
3.1. [Indent is important](#indent-is-important)\
3.2. [Comments](#comments)\
3.3. [Variables](#variables)\
3.4. [Primitive Built-in Types and Operators](#primitive-built-in-types-and-operators)\
3.5. [Interactive program](#interactive-program)

# Firsts Steps

## Introduction

Python is a **high-level**, **general-purpose** programming language. It is an **interpreted** language, that is, there is an interpreter capable of executing each instruction without previously compiling the program into machine-language instructions.

It supports :
* **Multi-paradigm programming**
Python supports procedural, declarative, object and functional programming. This guide will focus on the object paradigm.

* **Cross-platform**
Python interpreters exist in many operating systems such as Windows, Linux, MacOS, etc. This guide has been written from a Windows environment.

Python is **garbage-collected**, that is, we don't need to manage the memory manually (unlike C).

## Setup

### Download Python

In this guide, we will use Python 3. You can download it from the official website : [here](https://www.python.org/).

### PyCharm IDE

To write Python code, you need an editor. We can use simple editors such as Vim or Sublime Text but in this guide we will use an IDE (integrated development environment), which will help us a lot developping and running our programs.

PyCharm is an IDE developped by JetBrains (also known for other programming tools and IDE such as IntelliJ). You can download it from their official website : [here](https://www.jetbrains.com).

Be sure the IDE is pointing to the right interpreter (Python 3). When creating a new project you can open the ``Project Interpreter: New Virtualenv environment`` and checking the ``base interpreter`` field. If you have already created your project, you can check at ``File > Project:Name > Python Interpreter``.

PyCharm allows you to have an eye on your project files (on the left side usually) while developping. You can right-click on the project folder and click ``New > File`` to create your first script *My_First_Program.py* and start coding !

```python
print("Hello World !")
```

To execute your script, go on the top, and click ``Add Configuration...``. In the newly opened dialogue window, go on the left and click on ``+``, choose ``Python`` and set the name and the Script path to your script. You can also add parameters, which we will talk about later.

Accept the configuration and click on the play button. Enjoy !

PyCharm also supports a markdown editor (it will suggest you to install a plugin when editing a markdown file) that will interpret the file on the fly.

### Executing python scripts outside the IDE

You can also execute python files using the standard console of your computer. In an Unix system, you need to open a console and write this command :

```bash
# python3 path_to_file.py arg1 arg2
python3 My_First_Program.py # output : Hello World !
```

## Programming with Python

### Indent is important

Since Python doesn't use brackets, your code needs to be well indented to be understood by the interpreter.

```python
# good code
if True:
	print("one tab before this instruction means that we are inside the if")
print("same column as the if means that the instruction is outside the if")

# bad code
if True: # nothing will be done inside the if, so this statement is useless
print("hello")

if True:
		print("hello") # interpreter will cry at this and not know how to interpret it
```

### Comments

We can add comments a program, which will be visible only by the reader of the source code. Comments in Python are usually indicated by the ``#`` character, though we can also use quotes ``"""`` to make bloc comments.

```python
# this is a comment
# each line of a comment must start with # character

"""
	this is a bloc comment
	you can write everything you want
	using as many lines as you want
	keep it simple and clear though !
"""
```

### Variables

Usually, values aren't just used once and forgotten. You may want to use variables to keep their reference and use or even change the value.

You don't need to specify the type of the variable when declaring it ; since Python does dynamic typing, the type of the variable will be interpreted by the value given.

```python
name = "Zelda"
age = 25
```

Variable names can be whatever you want within some limits :

* Name has to begin with a letter
* Only letters, numbers and underscores are allowed

There are some naming conventions about variables. If you use PyCharm, the IDE itself will point at the name variable as a warning and suggest you conventional names for your variable. Do not hesitate to listen to your IDE and take the suggestion as a way to improve your coding style.

### Primitive Built-in Types and Operators

Primitive types are built-in, basic data structures.

* **Integer** represents whole numbers.

* **Float** represents decimal and rational numbers.

Integers and floats are lower, equal or higher than 0.

With the types above, you can do math operations such as ``+``, ``-``, ``*`` and ``/``. You also have the integer division ``//``, the modulo ``%`` and exponentiation ``**`` . You can use parenthesis to set the order of the operations.

```python
3 + 2.1       # 5.1
7 - 8         # -1
25 / 5        # 5.0
13 // 3       # 4
5 % 3         # 2
3 ** 2        # 9
(2 + 3) * 5   # 25
```

The above operators may be combined with an assignment operator ``=``.

```python
counter = 0    # 0
counter += 1   # 1
counter -= 3   # -2
counter *= -2  # 4
counter /= 2   # 2
```

* **Boolean** represents the True and False values.

With booleans, you can use logical operators such as ``and``, ``or`` and ``not``. 

```python
True and False   # False
True or False    # True
not True         # False
not False        # False
```

* **String** represents a sequence of characters.

```python
counter = 0                   # integer
counter2 = 1.2                # float
i_am_beautiful = True         # boolean
hello_world = "Hello World"   # string
hello_world2 = 'Hello World'  # string
```

Check below for operations with strings. Strings can also be manipulated as if they were lists (see [Python Structures](./python_structures.md)).

### Interactive program

As shown before, the function ``print()`` show you what was written inside in your standard console (whether it is in the terminal or the IDE's console).

Strings are written between ``' '`` or ``" "``.

You can also give to your ``print()`` function the name of a variable : if its value is easily interpreted as a string it will print the value directly, however, if the variable is an object, it will print its reference.

You can check the type of a variable by using the function ``type()``:

```python
my_object = MyObject()
print(type(my_object)) # will give you the object's type "MyObject"
```

You can append multiple strings to be printed at once, using the operator ``+``. If you want to append something that is not a string (an integer, for example), you need to use the function ``str()``.

```python
name = "Zelda"
age = 25
print("Hello, my name is " + name + "and I am " + str(age) + " years old")
```

We can also format a string with the method ``format()``.

```python
name = "Zelda"
age = 25
print("Hello World, I am {0} years old and my name is {1}.".format(age, name))
```

Python, as many (if not all) other languages, support user interaction with your program. To let the user speak, we can use the built-in function ``input()``.

```python
print("Hello, what is your name ?")
input_str = input()
print(input_str)
```

The ``input()`` function will read what the user writes in the console until the first end of line (EOL).