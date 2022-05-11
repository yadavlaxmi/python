# 3.Using sort function sort the given list?

def sort(a):
    i=0
    while i<len(a):
        j=0
        while j<len(a):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
            j+=1
        i+=1
    print(a)
sort([6,8,4,3,9,56,0,34,7,15])

# OUTPUT:-[6,8,4,3,9,56,0,34,7,15]