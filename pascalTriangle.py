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
Pascal Triangle has a special property of combinatrics 
and we are using combinatorics formula to solve the pascal triangle.
output to input 10
           1 
          1  1 
         1  2  1 
        1  3  3  1 
       1  4  6  4  1 
      1  5  10  10  5  1 
     1  6  15  20  15  6  1 
    1  7  21  35  35  21  7  1 
   1  8  28  56  70  56  28  8  1 
  1  9  36  84  126  126  84  36  9  1 


'''