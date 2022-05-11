# k)
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
i=5
while i>=1:
	j=5
	while j>=i:
		print(j-i+1,end=" ")
		j-=1
	print( )
	i-=1