#Q41. Write a Python program to find the list with maximum and minimum length.
#Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
#List with maximum length of lists:
#(3, [13, 15, 17])
#List with minimum length of lists:
#(1, [0])
def fun():
    list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    i=0
    c=0
    max=[]
    while i<len(list):
        if list[i]>max:
            max=list[i]
            c+=1
        i+=1
    j=0
    c1=0
    min=list[j]
    while j<len(list):
        if list[j]>max:
            min=list[j]
            c1+=1
        j+=1
    print((len(max),max))
    print((len(min),min))
fun()