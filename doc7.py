# 7. Write a program to print the sum of the first 10 Even numbers.
i=1
sum=0
while i<=10:
	if i%2==0:
		sum+=i
	i+=1
print(sum)