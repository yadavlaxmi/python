# 24.Remove duplicates from a list.
# List = [1,2,3,1,2,2]

# Output: [1,2,3]


n = [1,2,3,1,2,2]
i=0
duplicate=[ ]
while i<len(n):
	if n[i] not in duplicate:
		duplicate.append(n[i])
	i+=1
print(duplicate)