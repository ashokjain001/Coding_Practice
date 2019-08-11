
#perform binary search on a circular sorted array with distinct elements
#https://www.youtube.com/watch?v=uufaK2uLnSI&list=PL2_aWCzGMAwLPEZrZIcNEq9ukGWPfLT4A&index=4

def circularArraySearch(array,x):
	high = len(array)-1
	low = 0 

	while low<=high:
		mid = (low+high)/2

		print 'mid is ', mid
		
		if array[mid]==x:
			return 'value found at index ', mid

		#case 2: if middle element is less than the last element then the right half is sorted	
		if array[mid]<=array[high]: 

			print 'right half'

			if x>=array[mid] and x<=array[high]:
				low = mid+1
			else:
				high = mid-1
		
		#case 3: if the middle element is greater then the first element then the left half is sorted
		if array[mid] >= array[low]:

			print 'left half'

			if x >=array[low] and x<=array[mid]:
				high = mid-1
			else:
				low = mid+1


print circularArraySearch([11,12,15,18,2,5,6,8],8)