# 14.Write a function to check if a number is prime or not.
def fun():
    a=int(input("num"))
    i=1
    c=0
    while i<=a:
        if a%i==0:
            c+=1
        i+=1
    if c==2:
        print("prime num")
    else:
        print("not prime")
fun()