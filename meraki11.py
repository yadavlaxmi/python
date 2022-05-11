# Question 11

# Write a program to print the top 3 highest values of a given dictionary.
# Input :-

# my_dict = {
#  'a':50, 
#  'b':58, 
#  'c':56,
#  'd':40, 
#  'e':100, 
#  'f':20
#  }

# Visualize
# Output :-

# [58,56,100]

d= {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
i=0
max1=0
max2=0
max3=0

for i in d:
    if d[i]>max1:
        max1=d[i]
for j in d:
    if d[j]>max2 and d[j]<max1:
        max2=d[j]
for k in d:
    if d[k]>max3 and  d[k]<max2:
        max3=d[k]
print([max1,max2,max3])
