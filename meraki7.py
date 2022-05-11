import json
a=open("demofile.txt","r")
f=a.readlines()
i=0
m=[]
while i<len(f):
    j=f[i].split()
    m.append(j)
    i=i+1
i=0
n={}
while i<len(m):
    j=0
    while j<len(m[i]):
        n.update({m[i][0]:m[i][1]})
        j+=1
    i+=1
print(n)