from math import pi, sin
from operator import add, mul

radius = 10
area, circ = pi * radius * radius, 2 * pi * radius

def square(x):
	return mul(x, x)


def sum_square(x, y):
	return square(x) + square(y)


def area():
	return pi * radius * radius


f = min
f = max
g, h = min, max
max = g

result = max(f(2, g(h(1,5), 3)), 4) # min(max(2, min(max(1, 5), 3)), 4)
									# min(max(2, min(5, 3)), 4)
									# min(max(2, 3), 4)
									# min(3, 4)
									# 3
print(result)
