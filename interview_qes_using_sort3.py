def fun():
    list=["i","b","a","h"]
    i=0
    while i<len(list):
        j=0
        while j<len(list):
            if list[i]<list[j]:
                list[i],list[j]=list[j],list[i]
            j+=1
        i+=1
    print(list)
fun()
