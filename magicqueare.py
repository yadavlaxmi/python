#MAGIC SQUARE
ms=[
[8,3,4],
[1,5,9],
[6,7,2]
]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
while i<len(ms):
	r1+ms[i][0]
	r2+ms[i][1]
	r3+ms[i][2]
	c1+ms[i][0]
	c2+ms[i][1]
	c3+ms[i][2]
	i+=1
	if r1==r2==r3==c1==c2==c3:
		print('its magic square')
		break
	else:
		print('its not magic square')
		break