'''
1) Merge sort falls into the category of Divide and conquer
(we break a problem into subproblem, find solutions to the 
subproblems and using the solutions of the subproblem we 
construct solution to the actual problem)

2) This is a recursive algorithm - function calling itself
(reducing the problem in a self similar manner)

3) Stable sorting algorithm - it preserves the relative order of 
records with same key

4) It is not an in-place algoritm, Space Complexity is O(n)
memory or space complexity is proportional to the number of 
element in the list.

5) Time complexity - O(n log n)

'''

'''This function recursively calls itself to divide the array till size becomes one'''
def mergeSort(a):
	
	high=len(a)-1
	low=0
	mid=(low+high)/2

	if len(a)<2:
		print 'length of array is less than 2 and returning null'
		return 

	left = a[:mid+1]
	right = a[mid+1:]
	print 'splitting', a, 'into', left, right, low, mid, high, len(a)
	
	print 'calling left with array', left
	mergeSort(left)
	print ' '

	print 'calling right with array', right
	mergeSort(right)
	print ' '
	print 'calling merge with left', left, 'right', right, 'array', a
	return merge(left, right, a)


'''Helper function to merge 2 sorted arrays into one array'''
def merge(l,r,a): 

	
	nL=len(l)
	nR=len(r)

	i=0	
	j=0
	k=0

	while (i<nL and j<nR):
		if l[i]<=r[j]:
			a[k]=l[i]
			i+=1
		else:
			a[k]=r[j]
			j+=1
		k+=1

	while (i<nL):
		a[k]=l[i]
		i+=1
		k+=1

	while (j<nR):
		a[k]=r[j]
		j+=1
		k+=1
	print 'sorted array so far', a 
	return a	

print mergeSort([2,4,1,6,8,5,3,7])

'''
Output of the algorithm:
splitting [2, 4, 1, 6, 8, 5, 3, 7] into [2, 4, 1, 6] [8, 5, 3, 7] 0 3 7 8
calling left with array [2, 4, 1, 6]
splitting [2, 4, 1, 6] into [2, 4] [1, 6] 0 1 3 4
calling left with array [2, 4]
splitting [2, 4] into [2] [4] 0 0 1 2
calling left with array [2]
length of array is less than 2 and returning null
 
calling right with array [4]
length of array is less than 2 and returning null
 
calling merge with left [2] right [4] array [2, 4]
sorted array so far [2, 4]
 
calling right with array [1, 6]
splitting [1, 6] into [1] [6] 0 0 1 2
calling left with array [1]
length of array is less than 2 and returning null
 
calling right with array [6]
length of array is less than 2 and returning null
 
calling merge with left [1] right [6] array [1, 6]
sorted array so far [1, 6]
 
calling merge with left [2, 4] right [1, 6] array [2, 4, 1, 6]
sorted array so far [1, 2, 4, 6]
 
calling right with array [8, 5, 3, 7]
splitting [8, 5, 3, 7] into [8, 5] [3, 7] 0 1 3 4
calling left with array [8, 5]
splitting [8, 5] into [8] [5] 0 0 1 2
calling left with array [8]
length of array is less than 2 and returning null
 
calling right with array [5]
length of array is less than 2 and returning null
 
calling merge with left [8] right [5] array [8, 5]
sorted array so far [5, 8]
 
calling right with array [3, 7]
splitting [3, 7] into [3] [7] 0 0 1 2
calling left with array [3]
length of array is less than 2 and returning null
 
calling right with array [7]
length of array is less than 2 and returning null
 
calling merge with left [3] right [7] array [3, 7]
sorted array so far [3, 7]
 
calling merge with left [5, 8] right [3, 7] array [8, 5, 3, 7]
sorted array so far [3, 5, 7, 8]
 
calling merge with left [1, 2, 4, 6] right [3, 5, 7, 8] array [2, 4, 1, 6, 8, 5, 3, 7]
sorted array so far [1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]

'''









