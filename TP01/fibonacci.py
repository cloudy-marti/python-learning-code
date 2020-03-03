from upemtk import *
from math import pow

def fibonacci1(n) :
	"""
		Recursive fibonacci
		:param n:
		:return: result
	"""
	if n == 0 or n == 1:
		return n
	else:
		return fibonacci1(n-1) + fibonacci1(n-2)

nb = 10
print ("fibonacci of ({0}) = {1}".format(nb, fibonacci1(nb)))

def fibonacci2(n) :
	"""
		Recursive fibonacci that also informs of the number of calls
		:param n:
		:return: result, counter
	"""
	if n == 0 or n == 1:
		return n,1
	else:
		return fibonacci2(n-1)[0] + fibonacci2(n-2)[0], 1 + fibonacci2(n-1)[1] + fibonacci2(n-2)[1]

nb2 = 9
fiboArray = fibonacci2(nb2)

print ("fibonacci of ({0}) = {1}".format(nb2, fiboArray[0]))
print ("number of calls = {0}".format(fiboArray[1]))

def fibonacci3(n):
	if n == 0 or n == 1:
		return n,1
	else:
		fibo = fibonacci3(n-1)
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

def draw_fibo(nb,width,height,margin):
	previous_x = margin
	previous_y = height-margin

	for index in range(nb) :

		fibo = fibonacci2(index)

		fibo_x = (index*15)+margin
		fibo_y = height - (fibo[1]+margin)

		ligne(previous_x, previous_y, fibo_x, fibo_y, couleur="blue")
		cercle(fibo_x, fibo_y, 2, remplissage="black")

		previous_x = fibo_x
		previous_y = fibo_y

def draw_linear(nb, width, height, margin):
	previous_x = margin
	previous_y = height-margin

	for index in range(nb) :

		linear_x = (index*15)+margin
		linear_y = height - index - margin

		ligne(previous_x, previous_y, linear_x, linear_y, couleur="green")

		previous_x = linear_x
		previous_y = linear_y

def draw_exp(nb, width, height, margin):
	previous_x = margin
	previous_y = height-margin

	for index in range(nb) :

		exp_x = (index*15)+margin
		exp_y = height - (index*index) - margin

		ligne(previous_x, previous_y, exp_x, exp_y, couleur="red")

		previous_x = exp_x
		previous_y = exp_y

def draw_power(nb, width, height, margin):
	previous_x = margin
	previous_y = height-margin

	for index in range(nb) :

		exp_x = (index*15)+margin
		exp_y = height - (pow(2,index)) - margin

		ligne(previous_x, previous_y, exp_x, exp_y, couleur="yellow")

		previous_x = exp_x
		previous_y = exp_y

def display_fibo(width, height):

	cree_fenetre(width, height)

	margin = 5

	ligne(margin, margin, margin, height-margin)
	fleche(margin, height-margin, margin, margin)

	ligne(margin, height-margin, width-margin, height-margin)
	fleche(margin, height-margin, width-margin, height-margin)

	draw_fibo(15, width, height, margin)
	draw_linear(30, width, height, margin)
	draw_exp(30, width, height, margin)
	draw_power(30, width, height, margin)

	attente_clic()
	ferme_fenetre()

display_fibo(400, 400)