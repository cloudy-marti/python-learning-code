import sys


def ascii_print(ascii_character):
	for line in ascii_character:
		print(line)


def parse_letters(file, alphabet):
	ascii_char = 65  # A

	character = []

	for line in file:
		# completed character
		if len(character) == 8:
			alphabet[chr(ascii_char)] = character
			ascii_char += 1
			# clear character
			character = []
			# if we are done with maj letters, go to min letters
			if ascii_char == 91:
				ascii_char = 97
		# append the line without \n character
		character.append(line[:-1])
	alphabet[chr(ascii_char)] = character


def parse_numbers(file, alphabet):
	ascii_char = 48  # A

	character = []

	for line in file:
		# completed character
		if len(character) == 8:
			alphabet[chr(ascii_char)] = character
			ascii_char += 1
			# clear character
			character = []
		# append the line without \n character
		character.append(line[:-1])
	alphabet[chr(ascii_char)] = character


def parse_symbols(file, alphabet):
	symbols = (',', ';', ':', '!', '?', '.', '/', '"', "'", '(', '-', ')', '[', '|', ']')

	character = []
	index = 0
	for line in file:
		if len(character) == 8:
			alphabet[symbols[index]] = character
			index += 1
			if index >= len(symbols):
				break
			# clear character
			character = []
		# append the line without \n character
		character.append(line[:-1])
	alphabet[symbols[index-1]] = character


def get_max_len(character, alphabet):
	size = 0
	for line in alphabet[character]:
		if size < len(line):
			size = len(line)
	return size


def print_ascii_message(alphabet, msg):
	for i in range(0, 8):
		for character in msg:
			if character == " ":
				print("    ", end="")
			else:
				max_size = get_max_len(character, alphabet)
				letter = alphabet[character][i]
				letter += " "*(max_size-len(letter))
				print(letter, end="")
		print()


def print_ascii_message_with_max(alphabet, msg, max_size):
	line_size = 0
	sub_message = [[]]
	line_index = 0
	for character in msg:
		if character == ' ':
			if line_size + 4 <= max_size:
				line_size += 4
				sub_message[line_index] += character
		else:
			size = get_max_len(character, alphabet)
			tmp = line_size + size
			if tmp <= max_size:
				sub_message[line_index] += character
				line_size = tmp
			else:
				line_index += 1
				sub_message.append([])
				sub_message[line_index] += character
				line_size = size

	for messages in sub_message:
		print_ascii_message(alphabet, messages)


def message_is_valid(alphabet, message):
	for character in message:
		if character not in alphabet and character != " ":
			return False
	return True


def usage():
	print("ascii_art max_lenght message")


def ascii_art():
	if len(sys.argv) != 3:
		usage()
		return

	max_len = sys.argv[1]
	message = sys.argv[2]

	alphabet_path = "alphabet.txt"
	numbers_path = "chiffres.txt"
	symbols_path = "symbols.txt"

	with open(alphabet_path, 'r') as file:
		alphabet = {}
		parse_letters(file, alphabet)

	with open(numbers_path, 'r') as file:
		parse_numbers(file, alphabet)

	with open(symbols_path, 'r') as file:
		parse_symbols(file, alphabet)

	if not message_is_valid(alphabet, message):
		print("Supported characters are the following:")
		print(alphabet.keys())
		print("Please don't try to break my work :3")
		return

	# get a list of the alphabet
	ascii_maj = list(map(lambda x: chr(x), range(65, 91)))
	ascii_min = list(map(lambda x: chr(x), range(97, 123)))

	# print(ascii_maj)
	# print(ascii_min)

	# Exercise 1
	# print_ascii_message(alphabet, message)

	# Exercise 2
	print_ascii_message_with_max(alphabet, message, int(max_len))


ascii_art()
