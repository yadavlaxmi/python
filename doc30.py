def fun(a):
    i=0
    c=0
    while i<=a:
        if i%a==0:
            c+=1
    if c==2:
        print(c)
    i+=1
fun(20)
            