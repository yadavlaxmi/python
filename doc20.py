# 20.write a palindrome to check whether a number is palindrome r not
a=int(input("num"))
b=a
rvs=0
while a>0:
	c=a%10
	rvs=rvs*10+c
	a=a//10
if b==rvs:
	print("it is palindrom num")
else:
	print("it is not palindrom num")