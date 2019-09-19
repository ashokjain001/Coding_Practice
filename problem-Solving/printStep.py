# print step using for loop

def printStep(n):

	for i in range(n):
		str = ''
		for j in range(n):
			if j<=i:
				str = str+'#'
			else:
				str = str+' '
		print str
	return ''

print printStep(10)

# print step using recursion 

def printStep(n,str):
	str = str+'#'
	if n == 0:
		return ''
	else:
		print str		
		return printStep(n-1, str)

print printStep(10, ' ')
