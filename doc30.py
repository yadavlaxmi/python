# 30. Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms
a=int(input("num"))
i=1
sum=0
while i<=a:
	sum=sum+i**3
	i+=1
print(sum)