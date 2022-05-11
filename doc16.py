# Q16.Write a Python program to map two lists into a dictionary.

dic1={"name","age","gender"}
dic2={"swathi","14","female"}
dic3={}
for i in dic1:
    for j in dic2:
        dic3[i]=j
        dic2.remove(j)
        break
print(dic3)