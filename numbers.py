# Happy number:

# n=int(input('enter the num'))
# while n>9:
# 	sum=0
# 	while n>0:
# 		rem=n%10
# 		sum=sum+rem*rem
# 		n=n//10
# 	n=sum
# if n==1:
# 	print('happy')
# else:
# 	print('not happy')


 
# Harshad number.

# a=int(input("num"))
# b=a
# sum=0
# while b!=0:
# 	c=b%10
# 	sum=sum+c
# 	b=b//10
# if a%sum==0:
# 	print("harshad num")
# else:
# 	print("not harshad num")


# Strong number

# n=int(input("num"))
# tem=n
# sum=0
# rem=0
# while n>0:
# 	fact=1
# 	i=1
# 	rem=n%10
# 	while i<=rem:
# 		fact=fact*i
# 		i+=1
# 	sum=sum+fact
# 	n=n//10
# if sum==tem:
# 	print("strong num")
# else:
# 	print("not strong num")


# Duck number


# a=int(input("num"))
# n=0
# while a>0:
# 	b=a%10
# 	a=a//10
# 	if b==0:
# 		n+=1
# if n>=1:
# 	print("duck num")
# else:
# 	print("not duck num")


# Magic number


# a=int(input("num"))
# b=a
# sum=0
# while b>0:
# 	sum=b%10
# 	b=b//10
# if sum==1:
#    print("magic num") 
# else:
#    print("not magic num")


#  perfect number 
 
# a=int(input("num"))
# sum=0
# i=1
# while i<a:
# 	if a%i==0:
# 		sum=sum+i
# 	i+=1
# if sum==a:
# 	print("perfect num")
# else:
# 	print("not perfect num")


# Factor number


# a=int(input("num"))
# b=0
# while a>0:
# 	f=a*(a%10)
# 	a=a//10
# if a==b:
# 	print("factor num")
# else:
# 	print("not factor num")


