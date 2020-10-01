#!/usr/bin/python
import sys

def is_in_dict(dict_lines, word):
	for line in dict_lines:
		if line == word:
			return True
	return False

def main():
	lines = []
	with open(sys.argv[1], 'r', encoding='ISO-8859') as dict_file:
		lines = dict_file.readlines()
	for elt in sys.argv[2:]:
		if is_in_dict(lines, elt):
			print(elt + " found !")
		else:
			print(elt + " not found")

main()