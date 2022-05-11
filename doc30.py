# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
i=0
space={}
for i in dic:
	j=0
	st=''
	while j<len(i):
		if i[j]!=' ':
			st+=i[j]
		j+=1
	space[st]=dic[i]
print(space)