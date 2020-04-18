from tp01.distance.distance import *

import pickle

dist_memory = {}


def load_dictionary(file_path, series_list):
	file = open(file_path)
	show = [name for name in file]
	for s in series_list :
		print(s + "  ->  " + closest(s, show))
	file.close()


slist = ("Code Yolo", "North Park", "Game de tron")
load_dictionary("../series_2000-2019.txt", slist)
