# Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']


dic={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
a=[]
for b in dic:
    a.append(dic[b])
max1=0
for i in (range(len(a))):
    if a[i]>max1:
        max1=a[i]
max2=0
for j in (range(len(a))):
    if a[j]>max2:
        max2=a[j]
        
max3=0
for k in (range(len(a))):
    if a[k]>max3:
        if a[k]<max2:
            max3=a[k]
max4=0
for l in (range(len(a))):
    if a[l]>max4:
        if a[k]<max3:
            max4=a[l]
max5=0
for m in (range(len(a))):
    if a[m]>max5:
        if a[m]<max4:
            max5=a[m]
    
print(max1)
print(max2)
print(max3)
print(max4)
print(max5)


