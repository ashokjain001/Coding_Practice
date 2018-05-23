from math import factorial

def pascalTriangle(n):
	for i in range(n):
		val=''
		for j in range(i+1):
			val+=' '+str(factorial(i)/(factorial(j)*factorial(abs(i-j))))+' '
		print (' '*n)+val
		n-=1

print(pascalTriangle(10))

'''
Pascal Triangle has a special property of  
'''