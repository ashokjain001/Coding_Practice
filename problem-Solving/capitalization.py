#write a function that accepts a string. The function should 
#capitalize the first letter of each word in the string then 
#return the capitalized string.


def capitalization(string):
	array=string.split()
	newstr=''
	for i in array:
		newstr=newstr+' '+i[0].upper()+i[1:]
	return newstr
	
print capitalization('a short sentence')