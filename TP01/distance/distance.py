import cProfile


def distance1(str1, str2):
	if str1 == str2:
		return 0

	# case : empty string
	if len(str1) == 0:
		return len(str2)
	if len(str2) == 0:
		return len(str1)

	# case : last characters match
	if str1[0] == str2[0]:
		cost = 0
	else:
		cost = 1

	return min(cost + distance1(str1[1:], str2[1:]), 1 + distance1(str1, str2[1:]), 1 + distance1(str1[1:], str2))


dist_memory = {}


def distance2(str1, str2):
	if (str1, str2) in dist_memory:
		return dist_memory[(str1, str2)]
	if (str2, str1) in dist_memory:
		return dist_memory[(str2, str1)]

	dist = distance1(str1, str2)
	dist_memory[(str1, str2)] = dist

	return dist


def closest(string, possibilities):
	smallest_dist = 1024
	closest_str = "__not ok__"

	for index in range(len(possibilities)):
		dist = distance2(string, possibilities[index])
		if smallest_dist > dist:
			smallest_dist = dist
			closest_str = possibilities[index]

	return closest_str

"""
print("distance1 function result = {0}".format(distance1("abracadabra", "macabre")))

str_list = ("macabre", "acadabra", "bra", "henlo", "macabre", "coucou")

print("Searching for closest string between {0} and {1}".format("abracadabra", str_list))

print("dictionary should be empty")
print(dist_memory)
cProfile.run('closest("abracadabra", str_list)', sort='time')

print("dictionary should not be empty")
print(dist_memory)
cProfile.run('closest("abracadabra", str_list)', sort='time')
"""