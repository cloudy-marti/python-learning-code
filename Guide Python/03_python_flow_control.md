Python
=========================
Updated: 18/04/2020
[Return to Index](./00_python_index.md)

# Table of contents

1. [Introduction](#introduction)
2. [Comparison Operators](#comparison-operators)
3. [If Statement](#if-statement)
4. [While Loop](#while-loop)
5. [For Loop](#for-loop)\
5.1. [Enumerate Function](#enumerate-function)
6. [Break Statement](#break-statement)

# Flow Control

## Introduction

In a program you may need control flow statements that result in a choice between two or more paths. In order to make a choice, we need to perform one or more tests using comparison operators.

## Comparison Operators

A comparison operators perform some sort of test and returns True or False as a result. 

* Equal to ``==``
* Not equal to ``!=``
* Less than ``<``
* Greater than ``>``
* Less than or equal to ``<=``
* Greater than or equal to ``>``

Several tests can be done at once using the logical operators. See [Python Firsts Steps](./python_firsts_tests.md).

## If statement

The ``if`` statement is used as a form of conditional programming. You decide whether an instruction is executed or not based on the result of a test.

```python
counter = 0

if counter >= 0:
	print("I will be printed!")
```

You may give an additional instruction to be done in case the result of the test is ``False``, using the ``else`` statement:

```python
counter = 0

if counter == 1:
	print("I won't be printed...")
else:
	print("I will be printed!")
```

You can also give several conditions and several instructions to be done in each case, using the ``elif`` statement:

```python
counter = 0

if counter <= -1:
	print("I won't be printed...")
elif counter == 2:
	print("I won't be printed either...")
elif counter >= 3:
	pass # do nothing
else:
	print("I will be printed!")

print("Whatever happens before, I will be printed anyway.")
```

You can *nest* if statements inside another.

```python
counter = 0

if counter == 0 or counter == 1:
	if True:
		print("I will be printed!")
```

Overall, the generic code would be :

```python
if test:
	# do something
elif test:
	# do something
else:
	# do something
```

## While Loop

A ``while`` loop can be used to iterate through one or more code statements as long as the test condition is ``True``. The test is performed before each iteration, including the first one.

```python
counter = 0

# this code will print all numbers between 0 and 9 both included
while counter < 10:
	print(counter)
	counter += 1

print("End of loop !")
```

## For Loop

A ``for`` loop is used to iterate within a specific range.

We can use the built-in function ``range()``. The prototype of this function is ``range(included_first, non_included_last, step)``.

```python
# this code will print all numbers between 0 and 9 both included
for index in range(0, 10):
	print(index)

print("End of loop !")
```

The ``for`` loop allows us to iterate through a collection.

```python
my_collection = [1, 2, 3, 4, 5]

# this code will print all the elements of my_collection one by one
for element in my_collection:
	print(element)

print("End of loop !")
```

## ``Enumerate`` Function

We can also use the function ``enumerate()`` function to iterate through a collection with an index.

```python
my_collection = [3, 2, 3, 6, 1]

for index, element in my_collection:
	print(str(index) + " = " + str(element))

print("End of loop !")

''' Output :
	0 = 3
	1 = 2
	2 = 3
	3 = 6
	4 = 1
	End of loop !
'''
```

## Break statement

The statement ``break`` allows us to stop iterating no matter what and the program will keep executing if there are more instructions after the loop.

```python
counter = 1

while counter <= 200:
	counter *= 2
	print(counter)
	if counter >= 50:
		break

print("End of loop !")

''' Output :
	2
	4
	8
	16
	32
	64
'''
```