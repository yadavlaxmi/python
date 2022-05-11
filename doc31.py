# 31. Write a program to find the sum of following series:
# 1 + 2 + 6 + 24 + 120 . . . . . n terms
a=int(input("num"))
prod=1
i=1
sum=0
while i<=a:
	prod=i*prod
	print(prod,end="+")
	sum=sum+prod
	i+=1
print(sum)