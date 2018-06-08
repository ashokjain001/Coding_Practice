'''Find minimum difference between any two elements in an array
1) this algorithm has a running time of O(n^2) since there are 2 forloops.
'''

def minimumdifference(array):
  minimumvalue=max(array)
  for i in range(len(array)):
    for j in range(i+1,len(array)):
      if abs(array[i]-array[j])<minimumvalue:
        minimumvalue=abs(array[i]-array[j])
  return minimumvalue

#print minimumdifference([3,6,1,7,4,9,0,10])

#print minimumdifference([1, 5, 3, 19, 18, 25])

'''We can improve upon the solution by sorting the array first.
1) Sorting takes O(n log n) time.
2) Since there is one for loop the running time is O(n)
3) overall running time is O(n log n)
'''
def minimumdifference2(array):
  value=max(array)
  array=sorted(array)
  for i in range(len(array)-1):
    if (array[i+1]-array[i])<value:
      value=(array[i+1]-array[i])
  return value

#print minimumdifference2([3,6,1,7,4,9,0,10])
print minimumdifference2([1, 5, 3, 19, 18, 25, 25.7,25.6,25.05])