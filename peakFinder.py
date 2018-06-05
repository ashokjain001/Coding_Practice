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


print peakFinder([5, 10, 20, 15])
	
print peakFinder([10, 20, 15, 2, 23, 90, 67])

print peakFinder([10, 20, 30, 40, 50])

print peakFinder([100, 80, 60, 50, 20])



