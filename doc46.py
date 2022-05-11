# 46.Write a Python program to concatenate element-wise three given lists.
# Original lists:

# ['0', '1', '2', '3', '4']

# ['red', 'green', 'black', 'blue', 'white']

# ['100', '200', '300', '400', '500']

# Concatenate element-wise three said lists:

# ['0red100', '1green200', '2black300', '3blue400', '4white500']

list=[['0', '1', '2', '3', '4'],['red', 'green', 'black', 'blue', 'white'],['100', '200', '300', '400', '500']]
i=0
a=list[0]
b=list[1]
c=list[2]
d=[ ]
while i<len(a):
	j=0
	while j<len(b):
		k=0
		while k<len(c):
			e=a[i]+b[j]+c[k]
			d.append(e)

			k+=1
			j+=1
			i+=1
print(d)
