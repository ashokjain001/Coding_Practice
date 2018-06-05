'''
Count minimum steps to get the given desired array
consider an array with n elements and value of all
 the elements is zero. We can perform following 
 operations on the array.


https://www.geeksforgeeks.org/count-minimum-steps-get-given-desired-array/?qa-rewrite=7023/create-desired-array-from-zero-array

'''

def countSteps(array):
	
	s=sum(array)
	count=0
	while s!=1:
		if s%2==1:
			s-=1
			count+=1
		else:
			s=s/2
			count+=1
	return count+1 # final operation to convert array into zero
print countSteps([2,3])
print countSteps([2,1])
print countSteps([16,16,16])

