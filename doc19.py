# 19. Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!
a=int(input("num"))
sum=0
fact=1
i=1
while i<a:
	fact=fact*i
	sum=sum+i/fact
	i+=1
print("sum is:",round (sum,2))