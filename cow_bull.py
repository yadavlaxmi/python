# cow_bull

import random
print("WELL COME TO THIS GAME")
print("Name of this game:COWS AND BULLS")
print("This is like guessing game")
print("Rules of this game")
print("Rule number 1:Here you have only ten choices")
print("Rule number 2:If your guess is right then you are bull")
print("Rule number 3:If your guess is wrong then you are cow")
print("Are you ready!")
name=input("Enter your name:")
print(name)
def game():
    list=random.sample([0,1,2,3,4,5,6,7,8,9],5)
    print("you can start your game all the best")
    cows=[]
    bulls=[]
    for i in range(10):
        if bulls==list:
                print("WOWW your win")
                a=input("are you willing to play again yes or no")
                if a=="yes":
                    game()
                else:
                    print("Thanks for playing")
                break
        number=int(input("enter you guessed number:"))
        position=int(input("enter your guessing number positon:"))
        for i in list:
            if number in list:
               
                if number in list and list.index(number)==position:
                    bulls.insert(position,number)
                    print("Bull:",bulls)
                    break
                else:
                    cows.insert(position,number)
                    print("cow",cows)
                    break
            else:
                print("your number is not there in list")
                break
    else:
        print("sorry... your chances are over")
game()




                    