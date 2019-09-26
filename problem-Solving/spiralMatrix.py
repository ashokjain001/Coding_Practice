def spiralMatrix(n):

	counter = 1 

	row = 0 
	endrow = n-1
	column = 0
	endcolumn = n-1

	a = []
	for i in range(n):
		a.append([None]*n)

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

	return a

print spiralMatrix(3)
#[[1, 2, 3], [8, 9, 4], [7, 6, 5]]

print spiralMatrix(4)
#[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

print spiralMatrix(5)
#[[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]


