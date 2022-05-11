# 1.you have to print the largest value out of the given list using the max function?
def maximum(a):
    i=0
    mxm=0    
    while i<len(a):

        if a[i]>mxm:
            mxm=a[i]
        i+=1
    print(mxm)
maximum([3,5,7,34,2,89,2,5])



OUTPUT:-89