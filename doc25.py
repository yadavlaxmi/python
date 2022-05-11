# 25.Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3

# Output: [4, 3]

# Explanation: Both elements occur 4 times.

# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2

# Output: [4, 3, 6]

# Explanation: Occur 4, 3, and 3 times respectively


# A. 
n=[4,6,4,3,3,4,3,4,3,8]
i=0
a=[ ]
while i<len(n):
	j=0
	c=0
	while j<=i:
		if n[i]==n[j]:
			c+=1
		j+=1
	if c>3:
		a.append(n[i])
	i+=1
print(a)


# B. 
# n=[4,6,4,3,3,4,3,4,6,6]
# k=2
# a=[ ]
# while k<len(n):
# 	if n[k] not in a:
# 		a.append(n[k])
# 	k+=1
# print(a)