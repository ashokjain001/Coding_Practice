
'''Given a sorted array arr[] and a number x, 
write a function that counts the occurrences of x in arr[]. 
Expected time complexity is O(Logn)

Non Recursive implementation'''


def firstOccurence(l,low,high,val):

	while low<high:
		mid=low+(high-low)/2
 		print low, high, mid,l[mid], 'first occurrence'
 		if l[mid]<val:
 			low=mid+1
 		else:
 			high=mid

 	return low

def lastOccurence(l,low,high,val):
	
	while low<high:
		mid=int((low+high)/2)
  		print low, high, l[mid]
  		if l[mid]>val:
  			high=mid
  		else:
  			low=mid+1

  	return high	

def countOccurences(l,val):
	low=0
	high=len(l)-1

	first=firstOccurence(l,low,high,val)
	print first
	end=lastOccurence(l,low,high,val)

	return end-first

print(countOccurences([0,1,1,3,3,3,3,6,8,10,11,11],3))
