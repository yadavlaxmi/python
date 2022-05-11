# 47.Write a Python program to convert a given list of strings into list of lists.
# Original list of strings:

# ['Red', 'Maroon', 'Yellow', 'Olive']

# Convert the said list of strings into list of lists:

# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']



a=['red','maroon','yellow','white']
i=0
b=[ ]
while i<len(a):
	j=0
	m=[ ]
	while j<len(a[i]):
		m.append(a[i][j])
		j+=1
	i+=1
	b.append(m)
print(b)
