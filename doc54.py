# Q54.
#  Write a Python program to create a key-value list pairings in a given dictionary. 
#  Original dictionary:
#{1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
list={}
list1=[]
for i in dic:
    a=dic[i]
    for j in a:
        list[i]=j
print(list)