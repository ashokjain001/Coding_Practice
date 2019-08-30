def mindiff(a,b,t):
	mini = 1000
	for i in a:
		for j in b:
			diff=abs(t-(i+j))
			print i,j,diff, mini, t
			if diff<mini:
				print 'updating min with diff',mini,diff
				mini = diff
				
				x=i
				y=j
	return x,y,t

print mindiff([1,2,4,5,10,20],[-1,2,3,5,8,9],24)

def mindiff(a,b,t):
	i=len(a)-1	
	j=0
	while j <len(b) and i>=0:
		if (a[i]+b[j])<t:
			print a[i]+b[j],a[i],b[j], abs(t-(a[i]+b[j]))
			j=j+1
		if j<len(b) and (a[i]+b[j])>t and i>=0 :
			print a[i]+b[j],a[i],b[j], abs(t-(a[i]+b[j]))
			x=a[i]
			y=b[j]
			i = i-1	

	return x,y

#print mindiff([-1,2,3,5,8,9],[1,2,4,5,10,20],24)
#print mindiff([1,2,4,5,10,20],[-1,2,3,5,8,9],24)
#print mindiff([1,4,7,10],[4,5,7,8],13)
#print mindiff([4,5,7,8],[1,4,7,10],13)