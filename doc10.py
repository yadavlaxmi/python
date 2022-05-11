# 10.write a program to check wether the number is prime number or not?
a=int(input("num"))
i=1
b=0
while i<=a:
	if a%i==0:
		b+=1
	i+=1
if b==2:
	print("prime num")
else:
	print("not prime")