# t)
#          *
#         * *
#       *  *  *
#     *  *  *  *
#   * *  *  *   *   
a=int(input("num"))
i=0
while i<a:
	j=a-i-i
	while j>0:
		print(end=" ")
		j-=1
	star=i+1
	while star>0:
		print("*",end=" ")
		star-=1
	i+=1
	print( )