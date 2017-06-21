import math

def area(n, s):
	'''
	This function takes in two values, n an integer representing the number of sides,
	and s a number representing the length of each side.
	This function then returns the area.
	'''
    return (0.25 * n * s**2) / (math.tan(math.pi / n))

def perimeter(n, s):
	'''
	This function takes in two values, n an integer representing the number of sides,
	and s a number representing the length of each side.
	This function then returns the perimeter.
	'''
    return n * s

def polysum(n, s):
	'''
	This function takes in two values, n an integer representing the number of sides,
	and s a number representing the length of each side.
	This function returns the polysum which is PS = A + P^2
	'''
    return round(area(n, s) + perimeter(n, s)**2, 4)