# 17. Write a program to check whether a number is Armstrong or not.
a=int(input("num"))
b=a
sum=0
while a>0:
	c=a%10
	sum=sum+c*c*c
	a=a//10
if sum==b:
	print("amstrong")
else:
	print("not amstrong")