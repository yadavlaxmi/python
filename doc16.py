# 16. Write a program to print the factorial of a number accepted by the user.
a=int(input("num"))
fact=1
while a>0:
		fact=fact*a
		a-=1
print("factorial=",fact)