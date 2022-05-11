# write a code to call one function to another funtion?
def fun2(a,b):
    return(a+b)
def fun1(c):
    e=fun2(4,6)*c
    print(e)
fun1(10)
