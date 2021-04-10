from operator import add, sub


def a_plus_abs_b(a, b):
	if b < 0:
		b = b * -1
	
	return add(a, b)


def two_of_three(x, y, z):
	arr = [x, y, z]
	idx = 0
	max = 0
	for i in range(len(arr)):
		if arr[i] > max:
			max = arr[i]
			idx = i
	
	arr.pop(idx)
	return (arr[0] * arr[0]) + (arr[1] * arr[1])


def largest_factor(x):
	max = 0
	for i in range(1, x - 1):
		if x % i == 0:
			max = i
	
	return max


def hailstone(n):
	steps = 1
	while n != 1:
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
		steps = steps + 1
	
	return steps


steps = hailstone(27)
print(steps)
