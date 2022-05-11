# 10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

# "4",  "5" --> "9"
# "34", "5" --> "39"
# Notes:

# If either input is an empty string, consider it as zero.


def integers(a):
    i=0
    sum=0
    while i<len(a):
        sum=sum+a[i]
        i+=1
    print(sum)
integers([4,5])
integers([34,5])