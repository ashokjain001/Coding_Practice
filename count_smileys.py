'''Description:
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :] 

Example cases:

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
'''

#Solution
def count_smileys(arr):
    eyes = [':',';']
    nose=['-','~','','D',')']
    count = 0 
    for i in arr:
    	found = True
        for j, item in enumerate(i):
            if j==0 and item not in eyes:
            	found = False
            elif j>0 and item not in nose:
            	found = False

        if found == True:
            count+=1

    return count #the number of valid smiley faces in array/list

print(count_smileys([]))
print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

'''
Analysis - the code uses 2 nested loop of different size hence the runing time is O(n*m)
'''
