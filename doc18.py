# Q18.Write a Python program to get the maximum and minimum value in a dictionary.
dic={"a":20,"b":50,"c":40,"d":70}
dic1=list(dic.values())
max=0
i=0
while i<len(dic1):
    if dic1[i]>max:
        max=dic1[i]
    i+=1
print("maximum:",max)
min=dic1[0]
for i in dic1:
    if i<min:
        min=1
print("minimum:",min)