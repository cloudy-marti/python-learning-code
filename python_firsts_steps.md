Python
=========================
Updated: 18/04/2020

# Table of contents

1. [Introduction](#introduction)
2. [Setup](#setup)\
2.1. [Download Python](#download-python)\
2.2. [PyCharm IDE](#pycharm-ide)\
2.3. [Executing python scripts outside the IDE](#executing-python-scripts-outside-the-ide)\
3. [Version Control](#version-control)\
3.4. [Create a Project](#create-a-project)\
3.5. [Manage your project](#manage-your-project)
4. [Programming with Python](#programming-with-python)\
4.1. [Indent is important](#indent-is-important)\
4.2. [Comments](#comments)\
4.3. [Variables](#variables)\
4.4. [Primitive Built-in Types and Operators](#primitive-built-in-types-and-operators)\
4.5. [Interactive program](#interactive-program)\
4.6. [Commandline Arguments](#commandline-arguments)

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

## Version Control

This section is not a Python-specific tool. However, this is a powerful tool and every developer should learn to use it to keep track of their work, even when they are learning.

A version control tool is a system that tracks changes in source code during software development. It allows to keep the history of the changes and even collaborate with other developers on the same project.

The version control software that is used in this guide is ``GitHub`` as it is free, open source and widely used by the community but feel free to explore other version control software and choose the one you like the most.

Install ``git`` on your computer. You can download it [here](https://gitforwindows.org) for Windows. Install at least ``Git BASH``.

You can go on [GitHub](https://github.com) and create an account.

### Create a project

Click on the ``Start a Project`` button on your dashboard and you will be redirected. You will need to choose a Repository name like ``Python_Course`` and write a description if you want to.

You can choose to put your repository in public or in private. Private repositories are only visible by the owner and the collaborators of the project.

Usually you initialize the repository with a README and choose a ``.gitignore`` (in this case, search for the Python gitignore). This file will list all the files you don't need to save on the repository (such as binaries or the IDE configuration files) and keep your project clean.

Now you can click on ``Create repository`` and get started.

### Manage your project

Now that your project is created, you want to get a local copy on your computer so you can work on it. To do that, click on the ``Clone or download`` button and copy the URL it gives you. Then go to your workspace and open git bash, then type:

```bash
git clone URL_you_copied
```

Your repository has been created.

If you use PyCharm and want to keep your distant repository clean, open your .gitignore file and append at the end all the lines you find [here](https://github.com/github/gitignore/blob/master/Global/JetBrains.gitignore). This is a specific gitignore for all JetBrains IDE.

Now start by creating a project with PyCharm inside the newly cloned project. Create a file and write some code, then return to your git bash console to see the files you just created.

```bash
cd Python_Course\
# this will list your changes
git status
```

In order to update the changes you made locally in the distant repository, you need to stage your changes so they are ready to be commited.

```bash
# stage all of your changes
git add .
# or stage only the changes in a specific file
git add your_file.py
```

Then you want to capture a "snapshot" of your work, that is, the current state of your project.

```bash
# you must explain the reason of your commit
git commit -m "Started Work"
```

Now that you have your snapshot by the name of "Started Work" captured, you may want to update your distant repository with these changes.

```bash
# push changes into the distant repository
git push
```

Now get back to GitHub and reload the website. You can now see your modifications online !

If you need to work on this same project in another computer, just clone the project as shown above and repeat these steps. When you go back to the first computer, be sure to update your local copy of the project before doing any modification.

```bash
# retrieve the state of the distant repository
git pull
```

Everytime you make modifications, be sure to update your distant repository. By doing so, if anything happened to your computer, you won't ever lose your work, because it will be always available in your GitHub account.

This guide is available on my account: [here](https://github.com/hyliancloud/INFO_Python).

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

### Commandline Arguments

Another way to interact with the outside is to take in consideration parameters given within the commandline, when executing the program.

To do so, we need to import the library ``sys`` that will allow us to access the commandline. We will then be able to retrieve the arguments.

```bash
python3 hello.py hello World
```

```python
import sys

# get number of arguments
len(sys.argv)

# first element of argv is always the name of the script
program = sys.argv[0]

hello = sys.argv[1]
world = sys.argv[2]

print(hello + world + " !") # output : hello world !
```