def pyramid(n):

	for row in range(0,n):
		str = ' '
		for column in range(1,2*n):
			if  n-row <=column and n+row>=column:
				str = str+ '#'
			else:
				str = str + ' '
		print str 

print pyramid(4)
