# 36.
# Write a Python program to join adjacent members of a given list.
# Original list:

# ['1', '2', '3', '4', '5', '6', '7', '8']

# Join adjacent members of a given list:

# ['12', '34', '56', '78']

# Original list:

# ['1', '2', '3']

# Join adjacent members of a given list:

# ['12']

# A. 
list=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
a=[ ]
while i<len(list)-1:
	b=(list[i])+(list[i+1])
	a.append(b)
	i+=2
print(a)

# B. 

# list=['1', '2', '3']
# i=0
# a=[ ]
# while i<len(list)-1:
# 	b=(list[i])+(list[i+1])
# 	a.append(b)
# 	i+=2
# print(a)