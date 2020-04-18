Python
=========================
Updated: 18/04/2020\
[Return to Index](./00_python_index.md)

# Table of contents

1. [Introduction](#introduction)
2. [Files](#files)\
2.1. [Accessing Files](#accessing-files)\
2.2. [Read and Write Files](#read-and-write-files)

# IO and Files

## Introduction

Python programs may access the ``file system`` of the computer, which is the permanent data storage of the computer. The File Management System is responsible for managing the long term storage of data in files, whether it is locally on the computer or on flash drives.

Files store, not only the data, but also a set of ``attributes``, such as the date of last modification, size of file, but also ownership and permission access.

Files can be found through a ``path``, that can be ``absolute`` if it starts from the root directory of the computer, or ``relative`` if it starts from the workspace of the program.

## Files

### Accessing Files

The ``open(file_name, access_mode, buffering)`` method returns a file object which will be used to make operations with he file. Access_mode must be within the permissions your program has with the file.

The flags are :

| flag | Description                                                                                    |
|------|------------------------------------------------------------------------------------------------|
| r    | read-only, pointer at the beginning                                                            |
|      |                                                                                                |
| rb   | read-only in binary, pointer at the beginning                                                  |
|      |                                                                                                |
| r+   | read-write, pointer at the beginning                                                           |
|      |                                                                                                |
| rb+  | read-write, pointer at the beginning                                                           |
|      |                                                                                                |
| w    | write-only, overwrites file or creates a new one for write-only                                |
|      |                                                                                                |
| wb   | write-only in binary, overwrites file or creates a new one for write-only                      |
|      |                                                                                                |
| w+   | read-write, overwrites file or creates a new one for read-write                                |
|      |                                                                                                |
| wb+  | read-write in binary, overwrites file or creates a new one for read-write                      |
|      |                                                                                                |
| a    | opens a file for appending, pointer at the end or creates a new one in write-only              |
|      |                                                                                                |
| ab   | opens a file for appending in binary, pointer at the end or creates a new one in write-only    |
|      |                                                                                                |
| a+   | opens a file for appending and reading, pointer at the end or new file for read-write          |
|      |                                                                                                |
| ab+  | opens a file for appending and reading in binary, pointer at the end or new file in read-write |

After using the file, you should close it with the function ``close()``.

The best way to manipulate files in a Python program is using the ``with`` statement, which acts as the try-with-resources of Java, by opening the file and closing it automatically outside of its scope.

```python
with open(path, r) as file:
	# read file
# done
```

### Read and Write Files

* ``read()`` will return the content in a single string.

* ``readline()`` will return the next line including the newline character.

* ``readlines()`` will return a list of the lines.

The file is also iterable directly.

```python
with open(file, 'r') as file:
	all_data = read()
	print(all_data)

with open(file, 'r') as file:
	while True:
		line = file.readline()
		print(line)
		if not line:
			break

with open(file, 'r') as file:
	lines = readlines()
	for line in lines:
		print(line)

with open(file, 'r') as file:
	for line in file:
		print(line)
```

To write a file we must use the function ``write()``. This method does not add a newline character automatically.

```python
with open(file, 'w') as file:
	file.write("Hello World\n")
```