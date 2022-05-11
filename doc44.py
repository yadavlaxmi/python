# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

dic={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
dic0={}
dic1={}
dic2={}
dic3={}
for i in dic:
    dic0[i]=dic[i][0]
    dic1[i]=dic[i][1]
    dic2[i]=dic[i][2]
    dic3[i]=dic[i][3]
print([dic0,dic1,dic2,dic3])
    
