# Q40. Write a function For example, if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.


def fun():
    list=[9,1,1,9]
    i=0
    while i<len(list):
        sqr=list[i]*list[i]
        print(sqr,end="")
        i+=1
fun()
