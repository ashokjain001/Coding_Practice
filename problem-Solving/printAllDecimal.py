def printAllDecimalHelper(digit, s):
 	
	if digit==0:
		return s

	else:
		print printAllDecimalHelper(digit-1,s+'0')

		print printAllDecimalHelper(digit-1,s+'1')

		print printAllDecimalHelper(digit-1,s+'2')

		print printAllDecimalHelper(digit-1,s+'3')

		print printAllDecimalHelper(digit-1,s+'4')

		print printAllDecimalHelper(digit-1,s+'5')

		print printAllDecimalHelper(digit-1,s+'6')

		print printAllDecimalHelper(digit-1,s+'7')

		print printAllDecimalHelper(digit-1,s+'8')

		print printAllDecimalHelper(digit-1,s+'9')

	return ''

def printAllDecimal(digit):
	print printAllDecimalHelper(digit, '')

print printAllDecimal(3)