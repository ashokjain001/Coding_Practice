'''
Find lost element from a duplicated array
Given two arrays which are duplicates of each other except one element, that is one element from one of the array is missing, we need to find that missing element.

Examples:

Input:  arr1[] = {1, 4, 5, 7, 9}
        arr2[] = {4, 5, 7, 9}
Output: 1
1 is missing from second array.

Input: arr1[] = {2, 3, 4, 5}
       arr2[] = {2, 3, 4, 5, 6}
Output: 6
6 is missing from first array.
'''

'''First approach uses the sum operator and 
   difference is missing element between array'''
def missingElement(a,b):
  sum1 = sum(a)
  sum2 = sum(b)
  return 'Missing element is',abs(sum1-sum2)

print missingElement([2, 3, 4, 5,6,7],[2, 3, 4, 5, 6])

'''Second approach uses the binary search method and running time is improved'''
def missingElementBinary(a,b):
  print a,b
  high=len(a)
  low = 0
  mid=(low+high)/2
  if len(b)==0:
    print 'Missing Element is', a[mid]
    return 
  if a[mid-1]==b[mid-1]:
    missingElementBinary(a[mid:],b[mid:])
 
print missingElementBinary([2, 3, 4, 5, 6, 7,8],
                           [2, 3, 4, 5, 6,7])