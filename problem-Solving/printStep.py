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

#print printStep(10)

# print step using recursion 

def printStep(n,str):
	
	if n == 0:
		return ''
	else:	
		str = str+'#'
		print str
		return printStep(n-1, str)

#print printStep(10, ' ')


def printStep(n,row, str):

	if n == row:
		return

	if n == len(str):
		print str
		return printStep(n, row+1, '')

	else:
		if len(str)<=row:
			str = str+'#'
		else:
			str = str + ' '
		
		return printStep(n, row, str)

print printStep(4, 0,'')


