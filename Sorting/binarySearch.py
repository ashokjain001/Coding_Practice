'''
Binary search tree has a run time of n(log n) it cuts the 
array in half with every iteration unlike the linear search O(n) 
which iterates the whole array. For Binary search tree to work 
we need to provide sorted array as input.'''

def binarySearch(array,value):

	low=0
	high=len(array)-1
	
	while high>low:

		high=len(array)-1
		mid=(low+high)/2
		print 'Position -low', low, 'mid', mid, 'high', high

		if array[mid]==value:
			return array[mid], 'is found in the array'

		if array[mid]>value:
			print array[mid], 'is greater than', value
			array=array[:mid]
			print 'New array', array
		else:
			print array[mid], 'is less than', value
			array=array[mid+1:]
			print 'New array', array


print binarySearch([2,5,8,12,16,23,38,56,72,91],23)


''' 
Input:
Array - [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
search value - 23

Output:

Position - low 0 mid 4 high 9
16 is less than 23
new array [23, 38, 56, 72, 91]

Position - low 0 mid 2 high 4
56 is greater than 23
new array [23, 38]

Position - low 0 mid 0 high 1
(23, 'is found in the array')
'''