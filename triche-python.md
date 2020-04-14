Python
=========================
Updated: 14/04/2020


# Do not forget

1. Indent is important
```python
if True:
    print ("Dans le if")
    print ("Toujours dans le if")
print ("Pas dans le if")
```

2. String have to be between " or ' 
 
3. We execute the script with `python3 helloworld.py`

4. Comments are written after an #

5. Bloc comments are found between """:
```python
"""
    Write a comment that will be only read by the developper
"""
```

--------------------------------------------------------------------------------
# Structure
## If then else

Syntax:
```python
if test:
    ...
    ...
else:
    ...
    ...
```

Several conditions
```python
if test or test:
    ...
    ...
elif test and test:
    ...
    ...
else:
    ...
    ...
```

## `for` loop

> `for` are "for each" elements in a collection

1. `range`
```python
  for i in range(10):   # pour i dans [0,1,...9]
    print (i)
```

2. Iterate through a list
```python
  for element in ["Victor", "Nadime"]:
    print (element)
```

3. Iterate through a string
```python
  for c in "Hello World!"       #affiche une lettre par ligne, donc 12 en tout
    print(c);
```

4. Iterate through a file
```python
import sys
file = open("test.txt", "w")      # On ouvre le fichier "test.txt" en écriture
for x in [2**i for i in range(11)]:  # On écrit quelquechose dedans
  file.write(str(x)+"\n")           
file.close()                           # Puis, on ferme le fichier
file = open("test.txt","r")            # Et on le réouvre en lecture
for line in file:       # Pour chaque ligne dans `file`
  print (line, end='')    # la clause `end=''` indique de ne pas revenir à 
                          # ligne à la fin.
                          # En effet, chaque ligne termine déjà par un `\n`
```

5. Iterate with `enumerate`
```python
for index, element in enumerate(list) :
    # TODO
```

--------------------------------------------------------------------------------
# Collections

## `range`

* `range(10)` create the list [0,1,...,9]
* `range(3,10)` create the list [3,4,...,9] 
* `range(3,10,2)` create the list [3,5,7,9]
* `range(10,0,-1)` create the list [10,9,...,2,1]

Prototype:
                     `range( x,  y,  incr)`

# Dictionaries

> Structures indexed by a key. Each element corresponds to a key/value pair.

## Creation

```python
empty_dict = {}

dict0 = {
    'key1':'value1',
    'key2':'value2',
    ...,
    'key':'value'
}

dict1 = dict([
    ('key1', 'value1'),
    ('key2', 'value2'),
    ...
    ('key', 'value')
])
```

## Operations

```python
## Return the value associated to 'key'
dict['key']

## Add new key/value pair
dict['new_key'] = 'new_value'

## Remove a key/value pair from a dictionnary
dict.pop('key')

## More functions at : https://realpython.com/python-dicts/
```

# Tuples

> It is an inchangeable array
>
>* It has a fixed size.
>* Elements cannot be changed.

## Creation

```python
empty_tuple = ()

single_tuple = ('e',)

tuple1 = ('e1', 'e2', 'e3', ...)
```

## Value access
```python
index = 0

# get value at index :
tuple[index]

# get multiple values at index, index + 1, index + 2
tuple[index:index+2]

# get tuple values into variables
a, b, c = (1, 2, 3)
```

# Lists

## Creation
```python
empty_list = []

list0 = ["e1", "e2", ... , "e"]

# Elements can be of different types
list1 = ["e1", 0, 1.4, ['another', 'list']]
```

## Add and remove
```python
### Add e at the end of the list
list.append("e")

### Add e at any position i
list.insert(i, "e")

### Remove last element
list.pop()

### Remove element at position i
list.pop(i)
```

>* Tuple indexes begin with 0 ; a negative index means that we start counting by the end of the array.

## `*slice*`

>slice returns a copy of a part of the list.

```python
# Return list from index 1 to 4
list[1:4]

# Return list starting from index 2
list[2:]

# Return list from index 0 to index 4
list[:4]

# Deep copy of a list
list[:]
```

# `Set`
>Sets are collections that don't allow redundancy on their elements.

```python
# initialize an empty set
empty_set = set()

# initialize a set
my_set = {1, 1, 2, 4, 8, 8} # will be {1, 2, 4, 8}
```

## Operations

### Add elements
```python
empty_set = set()
empty_set.add(1)
empty_set.add(2)
empty_set.add(1) # won't be added
```

--------------------------------------------------------------------------------
# Display

## print()

>We can use print("str") to display a string

## Format

>We can format a string with the method .format(). We put the formatted arguments betwenen {} with the corresponding index.

```python
age=25
name=Bob
print("Hello World, I am {0} years old and my name is {1}.".format(age, name))
```

--------------------------------------------------------------------------------

# Function definition

## Function with one return value

```python
def func(arg1,arg2):
	"""
	TODO : implement function
	"""
	return res
```

## Functions with multiple return values

> These functions return a **tuple**.

```python
def func(arg1,arg2):
	"""
	TODO : implement function
	"""
	return res1,res2
```

--------------------------------------------------------------------------------

# Files

## Open file

```python
file = open(path_to_file, flag)
```

>Les flags sont les suivants : r, w, a, rb, wb (les derniers pour des données binaires)

## Read file

```python
for line in file
	for character in line
		# do something with the character
```

--------------------------------------------------------------------------------

# Parameters

## Arguments

```python
# python hello.py hello world

import sys

# get number of arguments
len(sys.argv)

# return the name of the script
sys.argv[0]

# return first argument
sys.argv[1]

```

## Variadic arguments

### *\*args*
> Allows several parameters to be passed to the function and be iterated

```python
def function(*args):
    for arg in args:
        # do something with each argument

function("e1", "e2", "e3", ...)
```

### *\*kwargs*
> Pass several arguments associated to a key

```python
def function(**kwargs):
    for arg in kwargs.values():
        # do something with each argument

function(a="e1", b="e2", c="e3", ...)
```

--------------------------------------------------------------------------------

