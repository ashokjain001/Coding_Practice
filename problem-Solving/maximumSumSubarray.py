
# solution is based on Kadane's Algorithm

def maximumSumSubarray(arr):
	sums = 0
	maxsum = 0
	for i in range(len(arr)):
		
		if sums+arr[i]>0:

			sums = sums+arr[i] 

			if sums>maxsum:

				maxsum = sums
		else: 
			sums = 0
			
	return maxsum


print maximumSumSubarray([1,-3,2,1,-1])

print maximumSumSubarray([3,-2,5,-1])

print maximumSumSubarray([1,-3,2,-5,7,6,-1,-4,11,-23])