def gcdIter(a, b):
	gcd = 1
	test = 1
	while test <= min(a,b):
		if a % test == 0 and b % test == 0:
			gcd = test
		test += 1
	return gcd

print(gcdIter(100,25))