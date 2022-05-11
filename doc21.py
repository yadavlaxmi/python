# 21. Write a python program  to sum the sequence:
# 1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!



n=int(input("num"))
sum=0
fact=1
i=1
while i<n:
    fact=fact*i
    sum=sum+i/fact
    i+=1
print("sum is:",sum)
    