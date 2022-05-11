# Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}


list=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dic1={}
a=[]
b=[]
c=[]
for i,k in list:
    if i=="yellow":
        a.append(k)
        dic1[i]=a
    elif i=="blue":
        b.append(k)
        dic1[i]=b
    elif i=="red":
        c.append(k)
        dic1[i]=c
print(dic1)
        