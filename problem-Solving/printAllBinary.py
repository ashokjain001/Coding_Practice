def printAllBinaryHelper(n, s):
	#print n, s 
	
	if n==0:
		#print s
		return s
	else:

		#print '0'
		#print 'first', n, s
		print printAllBinaryHelper(n-1, s+'0')

		#print '1'
		#print 'second ', n, s
		print printAllBinaryHelper(n-1, s+'1')

	return ''

def printAllBinary(n):

	print printAllBinaryHelper(n, '')

print printAllBinary(3)