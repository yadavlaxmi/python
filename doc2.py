# 2.Convert Character Matrix to single String;
#         The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]

# The String after join: gfgisbest

list= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
a=["g","f","g"]
b=["i","s"]
c=["b","e","s","t"]
list1=a+b+c

i=0
while i<len(list1):
	print(list1[i],end=" ")
	i+=1
