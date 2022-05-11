# 25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3


def fun():
    list=[2,-7,5,-64,-14]
    i=0
    count=0
    count1=0
    while i<len(list):
        if list[i]>0:
            count+=1
        else:
            count1+=1
        i+=1
    print("positive=",count)
    print("negative=",count1)
fun()
            