# Q14.Write a Python program to multiply all the items in a dictionary.

dic={"x":2,"y":3,"z":2}
sum=1
for i in dic:
    sum*=dic[i]
print(sum)