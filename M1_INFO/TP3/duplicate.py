#! /usr/local/bin/python3
'''duplicate.py: Program that searches for duplicate files.

Usage: duplicate.py [-h] [--help] [-e] [--extension] [extension] [-d] [--directory] [root] [-o] [--output] [output_file]
'''

import os, sys, getopt, hashlib

def usage():
	'Print usage doc and exit.'
	print (__doc__)
	sys.exit()


if __name__ == '__main__':

	try:
		optlist, arglist = getopt.getopt(sys.argv[1:], 'he:d:o:', ['help', '--extension=', '--directory=', 'output='])
	except:
		usage()

	if not optlist:
		usage()

	ext = root = ""
	for opt, arg in optlist:
		if opt in ['-h', '--help']: usage()
		elif opt in ['-e', '--extension']: ext = arg
		elif opt in ['-d', '--directory']: root = arg
		elif opt in ['-o', '--output']: output = arg
	
	duplicates = {}

	for root, dirs, files in os.walk(root):
		for file in files:
			path = os.path.join(root, file)
			try:
				with open(path, 'rb') as f:
					md5 = hashlib.md5(f.read()).hexdigest()
					if md5 in duplicates:
						duplicates[md5].append(path)
					else:
						duplicates[md5] = [path]
			except Exception as e: print(e)

	for md5, path_list in duplicates.items():
		if len(path_list) > 1:
			print()
			for path in path_list:
				print(path)
		
