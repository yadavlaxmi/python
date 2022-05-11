# Q34. Write a function which converts the input string to uppercase.
# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.


def fun():
    list=[10,14,2,23,19]
    list1=[99,2,2,23,19]
    i=0
    mxm=0
    sum=0
    while i<len(list):
        if  list[i]>mxm:
            mxm=list[i]
        else:
            sum=list[i]
        i+=1
    j=0
    mxm1=0
    sum1=0
    while j<len(list):
        if list[j]<mxm:
            if list[j]>mxm1:
                mxm1=list1[j]
        else:
            sum1=list[j]
        j+=1
    print("total",mxm+sum)
    print("total",mxm1+sum1)
fun()
                
    