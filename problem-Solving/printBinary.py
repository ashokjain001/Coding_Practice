def printBinary(n):

	if n==0:
		return

	else:
		print n, '0'
		print printBinary(n-1)

		print n, '1'
		print printBinary(n-1)


print printBinary(3)