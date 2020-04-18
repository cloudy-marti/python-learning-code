Python
=========================
Updated: 18/04/2020

Welcome to the Python beginner guide !

1. [First Steps](./01_python_firsts_steps.md)
2. [First Program](./02_python_first_program.md)
3. [Flow Control](./03_python_flow_control.md)
4. [Functions](./04_python_functions.md)
5. [Collections](./05_python_collections.md)
6. [Object Oriented Programming](./06_python_object_orientation.md)

--------------------------------------------------------------------------------

# Files

## Open file

```python
file = open(path_to_file, flag)

# Cleanup resources after using the file
with open(path_to_file) as file:
	# TODO
```

>Flags : r, w, a, rb, wb

## Read file

```python
for line in file
	for character in line
		# do something with the character
```
