# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].

def fun(a):
    i=1
    even=[]
    while i<len(a):
        if i%2==0:
            even.append(i) 
        i+=1
    print(even,end=" ")
fun([1,2,3,4,5,6,7,8,9])