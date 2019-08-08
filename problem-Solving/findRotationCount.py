#programming interview question to 
#find out the number of rotations of a sorted array in O(log n) time using binary search.



def findRotationCount(array):

	low = 0 
	high = len(array)-1
	n = len(array)
	while low<high:

		#case 1: where low<high i.e array is sorted	
		mid = (low+high)/2	

		print low, high, mid

		if array[low]<array[high]:
			return low, array[low]

		#case 2: (minimum)pivot element is less than the previous and next element	
		next=(mid+1)%n
		prev=(mid+n-1)%n

		if array[mid]<=array[next] and array[mid]<=array[prev]:
			return mid, array[low]

		#case 3: if mid element is less than highest element then the array is sorted from medium 
		         #to the highest and lowest element cannot exist hence updating the high	
		if array[mid]<array[high]:
			high = mid-1 

		#case 4: if mid element is greater than the lowest element in the array then lowest element 
		         #doesnt exist in the left half of the array.
		if array[mid]>array[low]:
			low = mid+1

print findRotationCount([11,12,15,18,2,5,6,8]) 

	