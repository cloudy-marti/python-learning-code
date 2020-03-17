from utils.graphical.upemtk import *
from math import pow


def fibonacci1(n):
	"""
		Recursive fibonacci
		:param n:
		:return: result
	"""
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci1(n - 1) + fibonacci1(n - 2)


def fibonacci2(n):
	"""
		Recursive fibonacci that also informs of the number of calls
		:param n:
		:return: result, counter
	"""
	if n == 0 or n == 1:
		return n, 1
	else:
		return fibonacci2(n - 1)[0] + fibonacci2(n - 2)[0], 1 + fibonacci2(n - 1)[1] + fibonacci2(n - 2)[1]


def fibonacci3(n):
	"""
		Recursive fibonacci that also informs of the number of calls
		:param n:
		:return: result, counter
	"""
	if n == 0 or n == 1:
		return n, 1
	else:
		fibo = fibonacci3(n - 1)
		return fibo[1], fibo[0] + fibo[1]


"""
2.
	fibonacci1 function is slow because it calculates fibonacci for each number below n. Too much redundancy
	Total of fibonacci calls when n = 4 : 9
	fibonacci1(4)
		> fibonacci(3)
			> fibonacci(2)
				> fibonacci(1)
				> fibonacci(0)
			> fibonacci (1)
		> fibonacci(2)
			> fibonacci(1)
			> fibonacci(0)
"""

fibo_memory = {}


def fibonacci5(value):
	if value < 0:
		print("illegal value")
	elif value <= 1:
		return value
	else:
		if value not in fibo_memory:
			fibo_memory[value] = fibonacci5(value - 1) + fibonacci5(value - 2)
	return fibo_memory[value]


def draw_fibonacci(value, width, height, margin, color, function):
	previous_x = margin
	previous_y = height - margin

	for index in range(value):
		fibo = function(index)

		fibo_x = (index * value) + margin
		fibo_y = height - (fibo[1] + margin)

		ligne(previous_x, previous_y, fibo_x, fibo_y, couleur=color)
		cercle(fibo_x, fibo_y, 2, remplissage="black")

		previous_x = fibo_x
		previous_y = fibo_y


def draw_linear(nb, width, height, margin):
	previous_x = margin
	previous_y = height - margin

	for index in range(nb):
		linear_x = (index * nb) + margin
		linear_y = height - index - margin

		ligne(previous_x, previous_y, linear_x, linear_y, couleur="green")

		previous_x = linear_x
		previous_y = linear_y


def draw_exp(nb, width, height, margin):
	previous_x = margin
	previous_y = height - margin

	for index in range(nb):
		exp_x = (index * nb) + margin
		exp_y = height - (index * index) - margin

		ligne(previous_x, previous_y, exp_x, exp_y, couleur="red")

		previous_x = exp_x
		previous_y = exp_y


def draw_power(nb, width, height, margin):
	previous_x = margin
	previous_y = height - margin

	for index in range(nb):
		exp_x = (index * nb) + margin
		exp_y = height - (pow(2, index)) - margin

		ligne(previous_x, previous_y, exp_x, exp_y, couleur="yellow")

		previous_x = exp_x
		previous_y = exp_y


def display_fibo(width, height, color, function, value):
	cree_fenetre(width, height)

	margin = 5

	ligne(margin, margin, margin, height - margin)
	fleche(margin, height - margin, margin, margin)

	ligne(margin, height - margin, width - margin, height - margin)
	fleche(margin, height - margin, width - margin, height - margin)

	draw_fibonacci(value, width, height, margin, color, function)
	draw_linear(value, width, height, margin)
	draw_exp(value, width, height, margin)
	draw_power(value, width, height, margin)

	attente_clic()
	ferme_fenetre()


display_fibo(400, 400, "blue", fibonacci3, 30)