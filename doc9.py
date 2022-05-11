# 9.Find the First Maximum, Second maximum, Third maximum number from the List.



a=[10,20,30,40,50,60]
i=0
max=0
while i<len(a):
	if a[i]>max:
		max=a[i]
	i+=1

max1=0
j=0
while j<len(a):
	if a[j]<max:
		if a[j]>max1:
			max1=a[j]
	j+=1

max2=0
k=0
while k<len(a):
	if a[k]<max1:
		if a[k]>max2:
			max2=a[k]
	k+=1
print(max)
print(max1)
print(max2)


