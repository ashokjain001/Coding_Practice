'''
Time complexity - Quicksort has running time of O(n log n) as average case running time 
							  O(n^2) as worst case running time

Space complexity - In Place sorting, and memory used is proportional to the size of the array
'''

def quicksort(a, start, end):

	if start<end:
		pIndex=partition(a,start,end)
		print 'pIndex', pIndex
		print ' '
		
		print 'calling quicksort left array', a[start:pIndex-1], 'starting index', start, 'ending index', pIndex-1 
		quicksort(a, start, pIndex-1)
		
		print 'calling quicksort right array', a[pIndex+1: end], 'starting index', pIndex+1, 'ending index', end 
		quicksort(a, pIndex+1, end)
 
	return a

def partition(a, start, end):
	pivot = a[end]
	pIndex=start
	print ' '
	print 'array', a[start:end+1], 'starting index', start, 'ending index', end, 'pivot index', pIndex, 'pivot value', pivot
	for i in range(start, end):
		print a[i],'is compared with',pivot
		if a[i]<pivot:

			print a[i], 'is less than', pivot, 'swapping', a[i], 'with', a[pIndex] 

			a[i],a[pIndex]=a[pIndex],a[i]
			pIndex+=1

			print 'updated array after swap', a[start:end+1], 'updated pIndex', pIndex

	a[pIndex],a[end]=a[end],a[pIndex]
	print 'updated array after the end of partition', a[start:end+1], 'updated pIndex', pIndex
	return pIndex


print quicksort([7,2,1,6,8,5,3,4],0,7)

print quicksort([40,7,90,20,60,21,6,19],0,7)

