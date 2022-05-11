# 9.Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).


def sqr():
    i=1
    squr=[]
    while i<=30:
        a=i*i
        squr.append(a)
        i+=1
    print(squr,end=" ")
    
sqr()