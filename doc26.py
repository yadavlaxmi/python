# 26. Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms
a=int(input("num"))
b="2"
i=0
while i<a:
	print(b,end=" ")
	b+='2'
	i+=1