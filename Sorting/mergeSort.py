def mergeSort(a):
	
	high=len(a)
	low=0
	mid = (low+high)/2

	left = a[:mid]
	right = a[mid:]
	print left, right, low, mid, high
	if len(a)<2:
		return a


	mergeSort(left)
	mergeSort(right)
	merge(left, right, a)


'''Helper function to merge 2 sorted 
	arrays into one array'''
def merge(l,r,a): 

	nL=len(l)
	nR=len(r)

	i=0	
	j=0
	k=0

	while (i<nL and j<nR):
		if l[i]<=r[j]:
			a[k]=l[i]
			i+=1
		else:
			a[k]=r[j]
			j+=1
		k+=1

	while (i<nL):
		a[k]=l[i]
		i+=1
		k+=1

	while (j<nR):
		a[k]=r[j]
		j+=1
		k+=1
	return a	

print mergeSort([2,4,1,6,8,5,3,7])