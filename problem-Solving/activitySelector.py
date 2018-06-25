#activity selector problem using greedy algorithm

def activitySelector(start, finish):
	n = 0
	j = 0
	for i in range(len(start)):
			if start[i]> finish[j]:
				print start[i], finish[j]
				n+=1
				j=i
	return n


start  =  [1, 3, 0, 5, 8, 5]
finish =  [2, 4, 6, 7, 9, 9]

print activitySelector(start, finish)


