# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import*

def fact(n):
	if n<0 :
		print("error n < 0")
	else :
		x = 0
		v = 1
		while x < n:
			x =  x +1
			v = v*x
		return v
	pass

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
		delta = b*b-4*a*c
	#print(delta)
	if (delta ==0):
		return (-b/(2*a))
	elif (delta > 0):
		return ( (-b-sqrt(delta))/2*a  ,(-b+sqrt(delta))/2*a )
	elif(delta <0):
		print("no solutions")
	pass
	"""
	pass

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
