# 15. Write a program to print the Fibonacci series till n terms (Accept n from user)
a=int(input("num"))
x=0
y=1
z=0
while z<=a:
	print(z)
	x=y
	y=z
	z=x+y