# 30.Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:

# list1 = [2, -7, 5, -64, -14]

# Output: pos = 2, neg = 3


# Iist2 = [-12, 14, 95, 3]

# Output: pos = 3, neg = 1

# A. 
list1 = [2, -7, 5, -64, -14]
i=0
count=0
count1=0
while i<len(list1):
	if list1[i]>0:
		count+=1
	else:
		count1+=1
	i+=1
print('positive',count)
print('negative',count1)


# B. 
# list2= [-12,14,95,3]
# i=0
# count=0
# count1=0
# while i<len(list2):
# 	if list2[i]>0:
# 		count+=1
# 	else:
# 		count1+=1
# 	i+=1
# print('positive',count)
# print('negative',count1)