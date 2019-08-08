'''Python implementation of Insertion sort
insertion sort has a run time of O(n^2)
Description - the second element is compared with the
first element and is swapped if it is not in order. 
Similarly, we take the third element in the next iteration 
and place it at the right place in the subarray of the 
first and second elements (as the subarray containing the 
first and second elements is already sorted). We repeat 
this step with the fourth element of the array in the next 
iteration and place it at the right position in the subarray 
containing the first, second and the third elements. 
We repeat this process until our array gets sorted
'''

def insertionSort(array):
	l=len(array)
	for i in range(l-1):
  		position=i
  		while position+1>0:
	  		print array, array[position+1], 'is compared with ', array[position],'before swap'
	  		if (array[position]>array[position+1]):
	  			array[position+1],array[position]=array[position],array[position+1]
	  			print array,'After swap position', position
	        	position-=1
	return 'sorted array', array

print insertionSort([40,7,90,20,60,21,6,19])

''' Output
[40, 7, 90, 20, 60, 21, 6, 19] 7 is compared with  40 before swap
[7, 40, 90, 20, 60, 21, 6, 19] After swap position 0
[7, 40, 90, 20, 60, 21, 6, 19] 90 is compared with  40 before swap
[7, 40, 90, 20, 60, 21, 6, 19] 40 is compared with  7 before swap
[7, 40, 90, 20, 60, 21, 6, 19] 20 is compared with  90 before swap
[7, 40, 20, 90, 60, 21, 6, 19] After swap position 2
[7, 40, 20, 90, 60, 21, 6, 19] 20 is compared with  40 before swap
[7, 20, 40, 90, 60, 21, 6, 19] After swap position 1
[7, 20, 40, 90, 60, 21, 6, 19] 20 is compared with  7 before swap
[7, 20, 40, 90, 60, 21, 6, 19] 60 is compared with  90 before swap
[7, 20, 40, 60, 90, 21, 6, 19] After swap position 3
[7, 20, 40, 60, 90, 21, 6, 19] 60 is compared with  40 before swap
[7, 20, 40, 60, 90, 21, 6, 19] 40 is compared with  20 before swap
[7, 20, 40, 60, 90, 21, 6, 19] 20 is compared with  7 before swap
[7, 20, 40, 60, 90, 21, 6, 19] 21 is compared with  90 before swap
[7, 20, 40, 60, 21, 90, 6, 19] After swap position 4
[7, 20, 40, 60, 21, 90, 6, 19] 21 is compared with  60 before swap
[7, 20, 40, 21, 60, 90, 6, 19] After swap position 3
[7, 20, 40, 21, 60, 90, 6, 19] 21 is compared with  40 before swap
[7, 20, 21, 40, 60, 90, 6, 19] After swap position 2
[7, 20, 21, 40, 60, 90, 6, 19] 21 is compared with  20 before swap
[7, 20, 21, 40, 60, 90, 6, 19] 20 is compared with  7 before swap
[7, 20, 21, 40, 60, 90, 6, 19] 6 is compared with  90 before swap
[7, 20, 21, 40, 60, 6, 90, 19] After swap position 5
[7, 20, 21, 40, 60, 6, 90, 19] 6 is compared with  60 before swap
[7, 20, 21, 40, 6, 60, 90, 19] After swap position 4
[7, 20, 21, 40, 6, 60, 90, 19] 6 is compared with  40 before swap
[7, 20, 21, 6, 40, 60, 90, 19] After swap position 3
[7, 20, 21, 6, 40, 60, 90, 19] 6 is compared with  21 before swap
[7, 20, 6, 21, 40, 60, 90, 19] After swap position 2
[7, 20, 6, 21, 40, 60, 90, 19] 6 is compared with  20 before swap
[7, 6, 20, 21, 40, 60, 90, 19] After swap position 1
[7, 6, 20, 21, 40, 60, 90, 19] 6 is compared with  7 before swap
[6, 7, 20, 21, 40, 60, 90, 19] After swap position 0
[6, 7, 20, 21, 40, 60, 90, 19] 19 is compared with  90 before swap
[6, 7, 20, 21, 40, 60, 19, 90] After swap position 6
[6, 7, 20, 21, 40, 60, 19, 90] 19 is compared with  60 before swap
[6, 7, 20, 21, 40, 19, 60, 90] After swap position 5
[6, 7, 20, 21, 40, 19, 60, 90] 19 is compared with  40 before swap
[6, 7, 20, 21, 19, 40, 60, 90] After swap position 4
[6, 7, 20, 21, 19, 40, 60, 90] 19 is compared with  21 before swap
[6, 7, 20, 19, 21, 40, 60, 90] After swap position 3
[6, 7, 20, 19, 21, 40, 60, 90] 19 is compared with  20 before swap
[6, 7, 19, 20, 21, 40, 60, 90] After swap position 2
[6, 7, 19, 20, 21, 40, 60, 90] 19 is compared with  7 before swap
[6, 7, 19, 20, 21, 40, 60, 90] 7 is compared with  6 before swap
('sorted array', [6, 7, 19, 20, 21, 40, 60, 90])
'''