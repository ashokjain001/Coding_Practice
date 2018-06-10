def peakFinder(array):
	'''This algo has a running time of O(n)'''

	l=len(array)
	peak=[]

	for i in range(l-1):
		#check to see if first element is peak 
		if (i==0) and (array[i]>array[i+1]):
			peak.append(array[i])
		#check to see if the middle element is peak
		elif (array[i]>array[i+1]) and (array[i]>array[i-1]):
			peak.append(array[i])
		#check to see if the last element is peak
		elif (i+1==l-1) and (array[i]>array[i-1]):
			peak.append(array[i+1])

	return peak

#print peakFinder([5, 10, 20, 15])
	
#print peakFinder([10, 20, 15, 2, 23, 90, 67])

#print peakFinder([10, 20, 30, 40, 50])

#print peakFinder([100, 80, 60, 50, 20])




def peakFinderBinary(array, low, high):
	
	#high=len(array)-1
	mid=(low+high)/2
	peak=[]
	print array, high, low, mid, array[low:high+1], array[mid]

	#base case
	if ((mid==len(array)-1 or array[mid]>array[mid+1]) and (array[mid]>array[mid-1] or mid==0)):
		return mid
		
	if (array[mid]<array[mid-1]): #middle element is less than the left neighbor, peak is in the left half
		return peakFinderBinary(array, 0, mid)

	if (array[mid]<array[mid+1]): #middle element is less than the right neighbor, peak is in the right half
		return peakFinderBinary(array, mid+1,len(array))


print peakFinderBinary([21, 20, 15, 19, 18, 90, 67], 0, 7)






























