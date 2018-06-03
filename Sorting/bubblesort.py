'''Python implementation of Bubblesort
Bubble sort has a run time of O(n^2)
After each pass the largest element is pushed towards the end and the Iteration continues till all the elements are in correct position'''
def bubblesort(array):
  l=len(array)
  for i in range(l-1,-1,-1):
    for i in range(l-1):
      if array[i]>array[i+1]:
        array[i],array[i+1]=array[i+1],array[i]
    print array
  return array    

print bubblesort([40,7,90,20,60,21,6, 19])