# 29.Remove empty List from List                
# The original list is: [5, 6, [], 3, [], [], 9]

# List after empty list removal: [5, 6, 3, 9]


list=[5,6,[],3,[],[],9]
a=[ ]
for i in list:
	if i!=[ ]:
		a.append(i)
	else:
		continue
print(a)