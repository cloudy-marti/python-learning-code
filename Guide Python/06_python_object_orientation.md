Python
=========================
Updated: 18/04/2020\
[Return to Index](./00_python_index.md)

# Table of contents

1. [Introduction](#introduction)
2. [Classes](#classes)\
2.1. [Class Definition and Instanciation](#class-definition-and-instantiation)\
2.2. [Example](#example)

# Object Orientation

## Introduction

Object-oriented approach is supported by Python. We can create classes and instanciate them (like in Java or C++). This is the paradigm chosen for this guide but be aware that it is not the only one that is supported by Python.

Object-oriented programming provides a structure that bundle ``data`` (attributes) and ``operations`` performed on this data (instance methods) together in classes. Classes are accessed via objects.

## Classes

A ``class`` is a block that is used as a template to construct objects. Each ``object`` or ``instance`` of a class will have its own values for all the ``attributes`` of the class. The class can specify the common behaviour through ``instance methods`` and each instance can execute these methods.

### Class Definition and Instantiation

A class in Python has the following syntax:

```python
class myClass:
	__init__
	attributes
	methods
static_functions
```

The init method will specify how an object is instanciated. Static functions can also be defined outside of the class (in the same file). These functions don't need an instanciated object to be called.

### Example

```python
class Pokemon:

	def __init__(self, name, genre, life, attack_moves):
		self.name = name
		self.genre = genre
		self.life = life
		self.attack_moves = attack_moves

	def change_name(self, new_name):
		self.name = new_name

	def is_ko(self):
		return self.life == 0


pikachu = Pokemon("Pikachu", "female", 25, {"thunderbolt", "slam", "agility", "thunder"})
pikachu.change_name("Yoshi")
if pikachu.is_ko:
	print("too sad")
else:
	print(pikachu.name + ", go!") # Yoshi, go!
```

When printing an object, we get the name of the class and the memory address where it is kept. We can provide a default string that represents better our object through the ``__str__()`` instance method.

*This is a non-exhaustive guide to oriented-object programming approach as we don't talk about inheritance or other OOP subjects such as encapsulation.*