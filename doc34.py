# 34.
# Write a Python program to remove all the values except integer values from a given array of mixed values.
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']

# After removing all the values except integer values from the said array of mixed values: [12, 0]


list=[34.67,12,-94.89,"python",0,"c#"]
i=0
b=[]
while i<len(list):
	if type(list[i])==int:
		b.append(list[i])
	i+=1
print(b)
