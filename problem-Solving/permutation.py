
def permutation(l):
	newlist=[]
	for i in range(len(l)):
		str=l[i]

		for j in range(len(l)):
			if i!=j:
				str=str+l[j]
		newlist.append(str)
	return newlist

print permutation(['A','B','C'])
	
	
 