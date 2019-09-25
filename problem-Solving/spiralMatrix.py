def spiralMatrix(n):

	counter = 1 

	row = 0 
	endrow = n-1
	column = 0
	endcolumn = n-1

	a = []
	for i in range(n):
		a.append([None]*n)
	print a

	while row <=endrow and column<=endcolumn:
		
		for i in range(column, endcolumn+1):
			a[row][i] = counter
			counter+=1
		row+=1
	
		for i in range(row,endrow+1):	
			a[i][endcolumn]=counter
			counter+=1
		
		endcolumn-=1
		
		for i in range(endcolumn, column-1, -1):
			a[endrow][i] = counter
			counter+=1
		endrow-=1

		for i in range(endrow,row-1,-1):
			a[i][column]=counter
			counter+=1
	
		column+=1

	print a
	return a

print spiralMatrix(3)