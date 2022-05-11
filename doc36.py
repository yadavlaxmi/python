# 36. Accept two numbers from the user and display sum of even numbers between them(including both)
a=int(input("num"))
b=int(input("num"))
i=a
sum=0
while i<=b:
	if i%2==0:
		print(i)
		sum=sum+i
	i+=1
print("total","=",sum)