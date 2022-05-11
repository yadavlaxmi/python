# 33.Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]

# List Integer Summation : [3, 13, 17, 7]

# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7


# The original list is : [15, 81, 11, 234]

# List Integer Summation : [6,9,2,9]

# B. 
# list= [15,81,11,234]
# i=0
# b=[]
# while i<len(list):
# 	j=list[i]
# 	sum=0
# 	while j>0:
# 		rem=j%10
# 		sum=sum+rem
# 		j=j//10
# 	b.append(sum)	
# 	i+=1
# print(b)


# A. 
list= [12,67,98,34]
i=0
b=[]
while i<len(list):
	j=list[i]
	sum=0
	while j>0:
		rem=j%10
		sum=sum+rem
		j=j//10
	b.append(sum)	
	i+=1
print(b)