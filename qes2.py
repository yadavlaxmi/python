# 2.you have to print the sum of the elements of the given list by using the sum function?

def fun(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i+=1
    print(sum)
fun([1,2,3,4,5])

OUTPUT:15
    