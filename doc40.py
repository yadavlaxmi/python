# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

list=['S001', 'S002', 'S003', 'S004']
list1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list2=[85, 98, 89, 92]
list3={}
for i in list1:
    for j in list2:
        if i in list1:
            list3[i]=list1[i]+list2[i]
        elif i not in list1:
            list3[j]=list1[j]
# a=[{i:j} for i,j in zip{dic1,dic2}]
# b=[{i,j} for i,j in zip{dic2,0}]
print(list3)        

