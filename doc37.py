# 37.
# Write a Python program to pair up the consecutive elements of a given list.
# Original lists:

# [1, 2, 3, 4, 5, 6]

# Pair up the consecutive elements of the said list:

# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

# Original lists:

# [1, 2, 3, 4, 5]

# Pair up the consecutive elements of the said list:

# [[1, 2], [2, 3], [3, 4], [4, 5]]

# A. 

list=[1, 2, 3, 4, 5, 6]
i=0
a=[ ]
while i<len(list)-1:
	b=[list[i],list[i+1]]
	a.append(b)
	i+=1
print(a)


# B. 

# list=[1, 2, 3, 4, 5, ]
# i=0
# a=[ ]
# while i<len(list)-1:
# 	b=[list[i],list[i+1]]
# 	a.append(b)
# 	i+=1
# print(a)