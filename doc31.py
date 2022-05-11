
# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

dic={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
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
        if a[j]<max1:
            max2=a[j]
max3=0
for k in (range(len(a))):
    if a[k]>max3:
        if a[k]<max2:
            max3=a[k]
print("item4",max1)
print("item1",max2)
print("item3",max3)