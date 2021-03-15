from operator import add, sub, mul


def a_plus_abs_b(a, b):
	"""Question 1. Return a+abs(b) but without calling abs"""
	if b < 0:
		f = add(a, mul(b, -1))
	else:
		f = add(a, b)
	
	return f


def two_of_three(a, b, c):
	"""Question 2. Return x*x + y*y, where x and y are the two largest members of the
	positive numbers a, b, and c."""
	list = [a, b, c]
	min_num_index = list.index(min(list))
	list.pop(min_num_index)
	
	return (list[0] * list[0]) + (list[1] * list[1])


def largest_factor(n):
	"""Question 3. Return the largest factor of n that is smaller than n."""
	last = 0
	if n < 1:
		pass
	elif n == 1:
		last = 1
	else:
		for i in range(1, n):
			if n % i == 0:
				last = i
	
	return last


result = largest_factor(15)
print(result)
