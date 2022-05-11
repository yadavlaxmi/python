# 5.Write a Python function that takes a list and returns a new list with unique elements of the first list.


# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].


def fun():
    list=[1,2,3,3,3,3,4,5]
    i=0
    duplicate=[]
    while i<len(list):
        if list[i] not in duplicate:
            duplicate.append(list[i])
        i+=1
    print(duplicate)
fun()