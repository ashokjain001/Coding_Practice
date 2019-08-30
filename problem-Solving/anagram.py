#check to see if 2 provided strings are Anagrams of each other.
#One string is an anagram of another if it uses the same characters 
#in the same quantity. Only consider characters, not spaces or
#punctuation.


def anagram(str1,str2):
	cmap1= anagramHelper(str1)
	cmap2= anagramHelper(str2)

	if len(cmap1)!=len(cmap2):
		return False

	for i in cmap1:
		if cmap1[i]!=cmap2[i]:
			return True	
	return True	

def anagramHelper(str1):
	newstr=''
	cmap={}
	newstr = ''.join(i for i in str1 if i.isalnum())
	
	for i in newstr:
		if i in cmap:
			cmap[i]=cmap[i]+1
		else:
			cmap[i]=1 

	return cmap	

print anagram('ashok~!@#$','%^*()(*&^kohsa~!@#$')


