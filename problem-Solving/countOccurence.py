'''Given a sorted array arr[] and a number x, 
write a function that counts the occurrences of x in arr[]. 
Expected time complexity is O(Logn)
Recursion implementation'''


def firstOccurence(l,low,high,val):

  start=low

  if len(l[low:high])<2:
  	print 'length is less than 2', l[low:high], start
  	return start

  mid=int((low+high)/2)

  print(low, mid, high, l[low:mid])

  if l[mid]==val:
  	return firstOccurence(l,low,mid,val)
 
  if l[mid]<val:
  	print l[mid],' is less than ',val
  	return firstOccurence(l,mid+1,high,val)

  if l[mid]>val:
  	print l[mid],' is greater than ',val
  	return firstOccurence(l,low,mid-1,val)
  
  return start

def lastOccurence(l,low,high,val):

  end=low

  if len(l[low:high])<2:
  	print('length is less than 2', l[low:high])
  	return end

  mid=int((low+high)/2)

  print(low, mid, high, l[low:mid])

  if l[mid]==val:
  	return lastOccurence(l,mid,high,val)
 
  if l[mid]<val:
  	print(l[mid],' is less than ',val)
  	return lastOccurence(l,mid+1,high,val)

  if l[mid]>val:
  	print(l[mid],' is greater than ',val)
  	return lastOccurence(l,low,mid-1,val)
  
  return end	

def countOccurences(l,val):
	low=0
	high=len(l)-1

	first=firstOccurence(l,low,high,val)
	end=lastOccurence(l,low,high,val)

	return end-first+1

print(countOccurences([0,1,1,3,3,3,3,6,8,10,11,11],3))
