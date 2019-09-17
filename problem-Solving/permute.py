
def permuteHelper(arr, chose):
	print arr, chose,'start'

	global call
	call+=1
	if len(arr)==0:
		print chose, 'len0'

	else:
		for i in range(len(arr)):

			#choose
			print arr,chose, 'inside1'
			chose.append(arr[i])
			arr.pop(i)
			print arr, chose, 'inner', i

			#explore
			permuteHelper(arr, chose)
			print 'outside', arr, chose
			#unchoose
			p=chose.pop()
			arr.insert(i,p)

			print arr, 'arr',chose,'chose', 'outer',i

call=0
def permute(arr):
	
	print permuteHelper(arr,[])
	print call 
print permute(['a','s','h'])