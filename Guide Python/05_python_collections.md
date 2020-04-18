Python
=========================
Updated: 18/04/2020

# Table of contents

1. [Introduction](#introduction)
2. [Tuples](#tuples)\
2.1. [Creation](#tuple-creation)\
2.2. [Value Access](#tuple-value-access)
3. [Lists](#lists)\
3.1. [Creation](#list-creation)\
3.2. [Value Access](#list-value-access)\
3.3. [Add and Insert](#list-add-and-insert)\
3.4. [Remove and Pop](#list-remove-and-pop)
4. [Sets](#sets)\
4.1. [Creation](#set-creation)\
4.2. [Value Access](#set-value-access)\
4.3. [Add](#set-add)\
4.4. [Remove](#set-remove)
5. [Dictionary](#dictionary)\
5.1. [Creation](#dictionary-creation)\
5.2. [Operations](#dictionary-operations)

# Collections

## Introduction

Earlier in this guide we talked about built-in types such as ``integer``, ``float``, ``boolean`` and ``string`` (see [Python First Program](./python_first_program.md)). Here we will talk about built-in ``collection types`` that represent a containers of other types.

## Tuples

A **tuple** is an ``indexed``, ``immutable`` and ``ordered`` collection that allows duplicate members.

### Tuple Creation

Tuples are defined with parentheses and their members are separated by commas. You can also use the function ``tuple()`` to create a tuple from another collection. Members of the tuple can be of different types, even collection types.

```python
empty_tuple = ()

single_tuple = ('e',)

another_tuple = ('e1', 'e2', 'e3', ...)

tuple_from_list = tuple(my_list)
```

### Tuple Value Access

Values can be accessed by their index or through a ``for`` loop. You can get the lenght of a tuple using the ``len()`` function. You can also check if a member is on the tuple.

```python
my_tuple = (1, 2.3, 3, True, "hello", 6, (7, 3, "World"))
index = 0

# get value at index :
my_tuple[index] # 1

# get multiple values from index to index + 2
my_tuple[index+1:index+3] # 2.3, 3 and True

# get tuple values into variables
a, b, c = (1, 2, 3)

# iterate through the tuple
for member in my_tuple:
    print(member)

# get lenght
len(my_tuple)

# check if a member is present in the tuple
value = 6
if value in my_tuple
    print("yeah")
```

## Lists

A **list** is an ``indexed``, ``mutable`` and ``ordered`` collection that allows duplicate members.

### List Creation

Lists are defined with brackets and their members are separated by commas. You can also use the function ``list()`` to create a list from another collection. Members of the list can be of different types, even collection types.

Lists can be created with the function ``range()``.

```python
empty_list = []

single_member_list = ["e1"]

my_list = ["e1", 0, 1.4, ['another', 'list']]

list_from_tuple = list(my_tuple)

# range(first_included, last_non_included, step)
range(0, 10, 2)   # [0, 2, 4, 6, 8]
```

### List Value Access

Values can be accessed by their index or through a ``for`` loop. You can get the lenght of a list using the ``len()`` function. You can also check if a member is on the list.

```python
index = 2

# return third member of the list
my_list[index] # 1.4

# iterate through list
for member in my_list:
    print(member)

# Return list from index 1 to 4
list[1:4]
# Return list starting from index 2
list[2:]
# Return list from index 0 to index 4
list[:4]
# Deep copy of a list
list[:]

# get lenght of list
len(my_list)

# check if member is on a list
value = 6
if value in my_list:
    print("yeah")
```

### List Add and Append

You can use the ``append()`` method to add an object to the end of the list. The method ``extend()`` will append the members of another lists.

The method ``insert()`` will take an object and the index as an argument and will add the object in the chosen index, shifting the elements to the right.

Two lists can be concatenated with the operator ``+``.

```python
my_list = [1, 2, 3]

my_list.append(4)        # [1, 2, 3, 4]
my_list.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
my_list.insert(2, 7)     # [1, 2, 7, 3, 4, 5, 6]

another_list = [3, 4]

concatenated_list = another_list + my_list # [3, 4, 1, 2, 7, 3, 4, 5, 6]
```

### List Remove and Pop

The ``remove()`` method will remove the first occurrence of the list. The ``pop()`` method will remove the last element of the list.

```python
concatenated_list.remove(4)    # [3, 1, 2, 7, 3, 4, 5, 6]

concatenated_list.pop()        # [3, 1, 2, 7, 3, 4, 5]
```

## Sets

A **set** is a ``unindexed``, ``mutable`` and ``unordered`` collection that does NOT allow duplicate members.

### Set Creation

Sets are defined with curly brackets and their members are separated by commas. You can also use the function ``set()`` to create a set from another collection.

```python
empty_set = set()

my_set = {1, 1, 2, 4, 8, 8} # will be {1, 2, 4, 8}

set_from_list = set([1, 2, 3])
```

### Set Value Access

Sets can be iterated through a ``for`` loop and check if an element is in the set. The set lenght can be obtained with the ``len()`` function.

```python
for number in my_set:
    print(number)

value = 2
if value in my_set:

len(my_set) # get lenght
```

### Set Add

A new value can be added to a set with the function ``add()``. If multiple values need to be added to the set we can use the ``update()`` method.

```python
my_set = set()

my_set.add(3)                 # {3}
my_set.update((3, 4, 5, 6))   # {3, 4, 5, 6}
```

The set is unordered, so the members may be added in a different order.

### Set Remove

A member of the set can be removed through the function ``remove()``. The method ``clear()`` will empty the set.

```python
my_set.remove(10)    # will do nothing
my_set.remove(3)     # {4, 5, 6}
my_set.clear()       # {}
```

## Dictionary

A **dictionary** is a ``mutable`` and ``unordered`` collection whose members are ``indexed`` by a ``key``. This collection allows duplicate values but does NOT allow duplicate keys.

### Dictionary Creation

Dictionaries are defined with curly brackets and their members, which are separated by commas, are pairs ``key:value``. You can also use the function ``dict()`` that takes a ``**kargs`` as an argument to create a dictionary.

```python
empty_dict = {}

dict0 = {
    'key1':'value1',
    'key2':'value2',
    ...:...,
    'key':'value'
}

dict1 = dict([
    ('key1', 'value1'),
    ('key2', 'value2'),
    ...
    ('key', 'value')
])
```

### Dictionary Value Access

Values can be accessed via their associated key. You can iterate through the values by getting them first with the function ``values()``. We can also iterate through the keys. The lenght of the dictionary can also be found via the function ``len()``.

```python
dict0['key2'] # 'value2'

for value in dict0.values():
    print(value) # will print value1, value2 until value

for key in dict0:
    print(key)

len(dict0)
```

### Dictionary Add and Update Value

Adding a new Entry (or pair) or changing the value of a key is done the same way: if the key doesn't exists, it is added to the dictionary. If the key already exists, the value is changed.

```python
# adds the entry France:Paris to the dictionary
dict0['France'] = 'Paris'
# changes the France value
dict0['France'] = 'Perpignan'
```

### Dictionary Remove

An item can be removed using the ``pop()`` that takes a key as an argument. The method ``clear`` will empty the dictionary.

```python
dict0.pop('France') # remove the France:Perpignan pair
dict0.clear()
```