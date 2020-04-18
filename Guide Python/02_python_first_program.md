Python
=========================
Updated: 18/04/2020\
[Return to Index](./00_python_index.md)

# Table of contents

1. [Indent is important](#indent-is-important)
2. [Comments](#comments)
3. [Variables](#variables)
4. [Primitive Built-in Types and Operators](#primitive-built-in-types-and-operators)
5. [Interactive program](#interactive-program)
6. [Commandline Arguments](#commandline-arguments)

# Programming with Python

## Indent is important

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

## Comments

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

## Variables

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

## Primitive Built-in Types and Operators

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

## Interactive program

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

## Commandline Arguments

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