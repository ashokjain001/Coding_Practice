# Prime number generator using Sieve of Eratosthenes algorithm. 

def findPrimeNumber(n):
	is_Prime = (n+1)*[1]
	is_Prime[0]=0
	is_Prime[1]=0
	for i in range(2,n):
		if is_Prime[i]==1:
			for j in range(i*2,n+1, i):	
				is_Prime[j]=0
				
	return is_Prime
print findPrimeNumber(15)

