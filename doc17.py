# 17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )

def fun():
    a=int(input("num"))
    if a>=18:
        print("eligible")
    else:
        print("not eligible")
        
fun()