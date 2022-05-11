def outer(a,c):
    s =a+c
    def inner(x,y):
        b = x-y
        print(b)
    inner(7,3)
    print(s)
outer(4,3)