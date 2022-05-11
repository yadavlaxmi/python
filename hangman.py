# hangman

import random
def hang():
    print("WELL COME TO THIS GAME")
    print("Name of this game:HANGMAN")
    print("This is like guessing game")
    print("Rules of this game")
    print("Rule number 1:Here you have only ten choices")
    print("Rule number 2:you have to guess letters from A-Z")
    print("Rule number 3:if you guess correct word then it will shows correct position")
    print("Rule number 4:if your guessing is wrong then will hang and after game is over")
    print("are you ready to play")
    print("you can start your game all the best")
    name=input("enter your name:")
    print("your name",name)
    list=["smiley","kalyan","shruthi","arun","ashwini","nandhini"]
    a=random.choice(list)
    b=set("abcdefghijklmnopqrstuvwxyz")
    print("guess the letter")
    guessing_letter= ''
    turns = 10
    while len(a)!=0:
        c=""
        for i in a:
            if i in guessing_letter:
                c+=i
            else:
                c+="_ "
        if c==a:
            print(c)
            print("congrats You Win")
            break
        print("you can guess now:",c)
        choose_letter = input("you have to guess a letter:")
        if choose_letter in b:
            guessing_letter+=choose_letter
        else:
            print("sorry the char is there in given set")
        if choose_letter not in a:
            turns-=1
            print("You have",turns,"choices only")
            if (turns == 9):
                print("|")
                print("|____")
            elif (turns == 8):
                print ("|")
                print ("|")
                print ("|")
                print ("|")
                print ("|____")
            elif (turns == 7):
                print ("___")
                print ("|	 |")
                print ("|")
                print ("|")
                print ("|")
                print ("|")
                print ("|____")
            elif (turns == 6):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|")
                print ("|")
                print ("|")
                print ("|____")
            elif (turns == 5):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	 |")
                print ("|	")
                print ("|")
                print ("|____")
            elif (turns == 4):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|")
                print ("|	 ")
                print ("|")
                print ("|____")
            elif (turns == 3):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 ")
                print ("|")
                print ("|____")
            elif (turns == 2):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|")
                print ("|____")
            elif (turns == 1):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|	/ ")
                print ("|____")
            elif (turns == 0):
                print ("___")
                print ("|	 |")
                print ("|	 O")
                print ("|	\|/")
                print ("|	 |")
                print ("|	/ \ ")
                print ("|____")
                print ("you guessed wrong ")
                print ("are you willing to play again?")
                play=input("Enter Yes or No:")
                if play=="Yes":
                    hang()
                else:
                    print("Thanks for playing!!")
                    break
                
                        
hang() 