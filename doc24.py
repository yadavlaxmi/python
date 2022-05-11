# 24. Write a program to display sum of odd numbers and even numbers separately that fall between two numbers accepted from the user.(including both numbers) 100 and 500.
a=int(input("num"))
b=int(input("num1"))
i=a
sum=0
sum1=0
while i<=b:
	if i%2==0:
		sum=sum+i
	else:
		sum1=sum1+i
	i+=1
print("sum of even=",sum,"sum of odd=",sum1)