from math import factorial

def pascalTriangle(n):
	for i in range(n):
		val=''
		for j in range(i+1):
			val+=str(factorial(i)/(factorial(j)*factorial(abs(i-j))))
		print val

print(pascalTriangle(10))