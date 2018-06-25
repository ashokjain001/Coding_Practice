'''Given a non-negative number represented as an array of digits, 
add 1 to the number ( increment the number represented by the digits ). 
The digits are stored such that the most significant digit is first element of array.

Examples :

Input : [1, 2, 4]
Output : [1, 2, 5]

Input : [9, 9, 9]
Output : [1, 0, 0, 0]
'''

def addOne(a):
	carry=1
	for i in range(len(a)-1,-1,-1):
		
		if a[i]==9:
			a[i]=0
		else:
			a[i]=a[i]+carry
			carry=0

	if carry==1:
		a=[1]+a	
	return a 


print addOne([1,9,9,9])
print addOne([9, 9, 9])