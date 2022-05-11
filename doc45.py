# 45. Write a Python program to remove the last N number of elements from a given list.
# Original lists:

# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]

# Remove the last 3 elements from the said list:

# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]

# Remove the last 5 elements from the said list:

# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]

# Remove the last 1 element from the said list:

# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]

# A. 


list=[2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
i=0
a=[ ]
while i<len(list)-3:
	if list[i]!=0:
		a.append(list[i])
	i+=1
print(a)
