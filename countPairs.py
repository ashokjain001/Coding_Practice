'''Given an array of integers, and a number sum, 
find the number of pairs of integers in the arra
whose sum is equal to sum'''

def countPairs(array, sum):
	l=len(array)
	count = 0
	for i in range(l):
		for j in range(i+1,l):
			if array[i]+array[j] == sum:
				count+=1
	return count

#print countPairs([1, 5, 7, -1],6)

