# 4.
# List product excluding duplicates.
#         List = [6,1,3,5,6,3,1]

#         Output: 60


list = [6,1,3,5,6,3,1]
i=0
duplicate=[ ]
while i<len(list):
	if list[i] not in duplicate:
		duplicate.append(list[i])
		a=duplicate[i]*i*i+list[i]*i
	i+=1
print(a)