'''Convert an array to reduced form | Set 1 
https://www.geeksforgeeks.org/convert-an-array-to-reduced-form-set-1-simple-and-hashing/
Given an array with n distinct elements, convert the given array to a form where all 
elements are in range from 0 to n-1. The order of elements is same, i.e., 0 is placed 
in place of smallest element, 1 is placed for second smallest element, n-1 is placed 
for largest element.
Since there is one for loop, running time of this algorithm is O(n)
'''
def reduceFunction(array):
  newarray=['']*len(array)
  j=0
  for i in range(len(array)):
    minIndexVal=array.index(min(array))
    array[minIndexVal]=array[minIndexVal]*100
    newarray[minIndexVal]=j
    j+=1
  return newarray

#print reduceFunction([10,40,20])
#print reduceFunction([5, 10, 40, 30, 20])->[0, 1, 4, 3, 2]
#print reduceFunction([841, 315, 752, 544, 437, 646, 165, 718, 773, 798, 872, 329, 602, 726, 687, 476, 664, 631, 672, 474, 724, 313 ])

#using python dictionary
def reduceFunction2(array):
  arraysorted=sorted(array)
  j=0
  d={} #initializing dictionary
  # for loop to store key value of the sorted array
  for i in arraysorted:
    d[j]=i
    j+=1
  # loop the original array and match value to dictionary & create a new array in reduced form 
  newarray=[] # new array to return the reduced function
  for i in array:
    newarray.append(d.keys()[d.values().index(i)]) #accessing dictionary key using array value
  return newarray

#print reduceFunction2([5, 10, 40, 30, 20])
print reduceFunction2([841, 315, 752, 544, 437, 646, 165, 718, 773, 798, 872, 329, 602, 726, 687, 476, 664, 631, 672, 474, 724, 313 ])