# 5.Use the min function and find the minimum value of the list?

def min(a):
    i=0
    b=0
    c=a[i]
    while i<len(a):
        if a[i]<c:
            c=a[i]
            b+=1
        i+=1
    print(c)
min([8,6,4,8,4,50,2,7])


OUTPUT:-2