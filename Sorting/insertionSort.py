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

def insertionSort(A):

  for i in range(len(A)-1):
      position=i
      while position+1>0:
      	print A,position, 'Before Iteration'
        if A[position+1]<A[position]:
          A[position+1],A[position]=A[position],A[position+1]
          print A, position, 'After Iteration'
        position-=1
        
  return A

print insertionSort([40,7,90,20,60,21,6, 19])
