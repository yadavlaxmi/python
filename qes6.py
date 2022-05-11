def fun():
    a=([5,10,50,20])
    b=([2,20,3,5])
    i=0
    c=[]
    while i<len(a):
        list=a[i]*b[i]
        c.append(list)
        i+=1
    print(c)
    
fun()
    