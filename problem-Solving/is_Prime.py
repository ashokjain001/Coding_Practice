#if n has no factor till sq root of then it will have no factor 
#after sq root of n and we can loop only till sqrt of n 

from math import sqrt
from math import ceil

def is_Prime(n):
	s = sqrt(n)
	s = int(ceil(s))
	print s
	for i in range(2,s):
		if n%i==0:
			return n, 'Not a prime number'	
	return n,'is a prime number'		

print is_Prime(54)