def gcdRecur(a, b):
	if b == 0:
		gcd = a
	else:
		gcd = gcdRecur(b, a % b)
	return gcd

print(gcdRecur(10,25))