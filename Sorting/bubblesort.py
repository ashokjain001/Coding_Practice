'''Python implementation of Bubblesort
Bubble sort has a run time of O(n^2)
After each pass the largest element is pushed towards the end and the Iteration continues till all the elements are in correct position'''
def bubblesort(A):
  for i in range(len(A)-1,-1,-1):
    for i in range(len(A)-1):
      if A[i]>A[i+1]:
        A[i],A[i+1]=A[i+1],A[i]
    print A
  return A    

print bubblesort([40,7,90,20,60,21,6, 19])