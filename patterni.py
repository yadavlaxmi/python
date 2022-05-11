# i)
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
i=1
while i<=5:
	j=1
	while j<=5-i:
		print(' ',end=" ")
		j+=1
	k=i
	while k>=1:
		print(i,end=' ')
		k-=1
	print( )
	i+=1