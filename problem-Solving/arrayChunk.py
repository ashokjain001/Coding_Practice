#Array chunk problem

def arraychunk(array, l):
	newarray=[]

	while len(array)>0:
		newarray.append(array[:l])
		del array[:l]
	return newarray

print arraychunk([1,2,3,4,5],4)
#print arraychunk([1,2,3,4,5,6,7],2)

