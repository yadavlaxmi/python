# 12. Write a program to find the product of the digits of a number accepted from the user.
a=int(input("num"))
prod=1
while a>0:
	prod=prod*(a%10)
	a=a//10
print(prod)