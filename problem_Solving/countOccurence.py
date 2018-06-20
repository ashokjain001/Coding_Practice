def countOccurence(l,low,high,val, count):
	print l[low:high+1]

	mid=(low+high)/2

	print low, mid, high
	
	if len(l[low:high])<2:
		count=+1
		return

	if l[mid]==val:

		countOccurence(l,low,mid,val, count)
		countOccurence(l,mid,high,val, count)

	if l[mid]<val:
		countOccurence(l,mid+1,high,val, count)

	if l[mid]>val:
		countOccurence(l,low,mid-1,val, count)
	return count

print countOccurence([0,1,1,3,3,3,3,6,8,10,11,11],0,11,3,0)