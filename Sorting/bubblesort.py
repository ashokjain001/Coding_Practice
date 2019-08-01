'''Python implementation of Bubblesort
Bubble sort has a run time of O(n^2)
After each pass the largest element is pushed 
towards the end and the Iteration continues 
till all the elements are in correct position'''
def bubblesort(array):
	l=len(array)
	for i in range(l-1):
		for j in range(l-1):
			if array[j]>array[j+1]:
				array[j],array[j+1]=array[j+1],array[j]
	return array

print bubblesort([40,7,90,20,60,21,6, 19])

''' Output
[7, 40, 20, 60, 21, 6, 19, 90]
[7, 20, 40, 21, 6, 19, 60, 90]
[7, 20, 21, 6, 19, 40, 60, 90]
[7, 20, 6, 19, 21, 40, 60, 90]
[7, 6, 19, 20, 21, 40, 60, 90]
[6, 7, 19, 20, 21, 40, 60, 90]
[6, 7, 19, 20, 21, 40, 60, 90]
[6, 7, 19, 20, 21, 40, 60, 90]
[6, 7, 19, 20, 21, 40, 60, 90]
'''
