def fun(str):
    i=0
    while i<len(str):
        j=0
        while j<len(str):
            if str[i]<str[j]:
                str[i],str[j]=str[j],str[i]
            j+=1
        i+=1
    print(str)
fun(["1234abcd"])
