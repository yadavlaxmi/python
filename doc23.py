# 23. Write a program to accept 10 numbers from the user and display the largest & smallest number.

i=1
while i<=9:
    i+=1
    a=int(input("num"))
    if a>=9:
        print("no guessed wrong")
    else:
        print("u guessed right")