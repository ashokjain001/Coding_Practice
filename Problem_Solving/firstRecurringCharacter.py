
'''Find the first recurring character in the given string!
This algorithm has a running time of O(n)'''

def firstRecurringCharacter(str):
	dict={}
	for i in str:
		if i in dict:
			return i
		else:
			dict[i]=1

print firstRecurringCharacter('BCABA')

'''
A variation of this problem: find the first NON-recurring character.
'''

def nonRecurringCharacter(str):
	dict={}
	for i in str:
		if i in dict: 
			dict[i]+=1
		else:
			dict[i]=1
	for i in dict:
		if dict[i]==1:
			return i,dict


print nonRecurringCharacter('eBCABAef')