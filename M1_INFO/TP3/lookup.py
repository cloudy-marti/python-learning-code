#! /usr/local/bin/python3

from Levenshtein import distance as levenshtein_distance

def candidate_len(word, l):
	return len(word.rstrip()) >= l-1 and len(word.rstrip()) <= l+1

def is_match(word, candidate):
	return levenshtein_distance.distance(word, candidate) <= 1

def lookup(word):
	with open('liste.de.mots.francais.frgut.txt', 'r', encoding='latin1') as fr_dict:
		# print(fr_dict.readlines())
		l = len(word)
		candidates = [x.rstrip() for x in fr_dict.readlines() if is_match(word, x.rstrip())]
		return candidates


print(lookup('ais'))