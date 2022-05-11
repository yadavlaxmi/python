# 1.Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.

def count():
    a=['abc','xyz','aba','1221']
    i=0
    c=1
    while i<len(a):
        if a[i]==a[-1]:
            c+=1
        i+=1
    print(c)
count()
