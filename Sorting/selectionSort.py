
'''
The selection sort algorithm sorts an array by repeatedly finding the minimum 
element (considering ascending order) from unsorted part and putting it at the 
beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element 
(considering ascending order) from the unsorted subarray is picked and 
moved to the sorted subarray.

Time Complexity: 
O(n2) as there are two nested loops.

Space Complexity: O(1)
The good thing about selection sort is it never makes more than O(n)
 swaps and can be useful when memory write is a costly operation.
 This is in-place sorting
'''
#Using helper function
def selectionSort(arr):
	print arr
	l=len(arr)
	for i in range(l):
		minval=min(arr[i:]) #find minimum value in the rest of the array
		minindex=arr.index(min(arr[i:])) #store the index of the minimum array
		arr[i], arr[minindex] = minval, arr[i]
		print arr
	return arr
#print selectionSort([2,7,4,1,5,3])


#Using for loop 
def selectionSort2(arr):
	print 'Input', arr
	l=len(arr)
	for i in range(l):
		for j in range(i,l): #finding minimum value in rest of the array
			if arr[j]<arr[i]: #compare the first element vs the rest of the element in the array
				print arr[j], 'is smaller than', arr[i], 'and swapped'
				arr[j],arr[i]=arr[i],arr[j]#swap value
				print arr
	return 'Output' ,arr
print selectionSort2([2,7,4,1,5,3])

'''
Input [2, 7, 4, 1, 5, 3]
1 is smaller than 2 and swapped
[1, 7, 4, 2, 5, 3]
4 is smaller than 7 and swapped
[1, 4, 7, 2, 5, 3]
2 is smaller than 4 and swapped
[1, 2, 7, 4, 5, 3]
4 is smaller than 7 and swapped
[1, 2, 4, 7, 5, 3]
3 is smaller than 4 and swapped
[1, 2, 3, 7, 5, 4]
5 is smaller than 7 and swapped
[1, 2, 3, 5, 7, 4]
4 is smaller than 5 and swapped
[1, 2, 3, 4, 7, 5]
5 is smaller than 7 and swapped
[1, 2, 3, 4, 5, 7]
('Output', [1, 2, 3, 4, 5, 7])
'''

