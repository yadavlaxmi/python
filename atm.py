def atm():
    print("wel come to atm")
    print("insert atm")
    pin=int(input("enter 4 digit pin number"))
    amt=5000
    def pin(x):
        print("0.balance enquiry")
        print("1.amount withdraw")
        print("2.amount deposit")
        print("3.change the pin")
        print("4.collect amount")
        print("5.quit")
    pin(2000)
    choose0=int(input("choose transaction"))
    def choose0(a):
        a=int(input("balance enquiry"))
        if a<=5000:
            print("valid balance")
        elif a>=5000:
            print("invalid balance")
        else:
            print("transaction completed")
    choose0(1)
    def choose1(b):
        b=int(input("amount withdraw"))
        if b<=5000:
            print("take your amount")
        elif b>=5000:
            print("sorry balance not avilable")
        else:
            print("thank you")
    choose1(2)
    def choose2(c):
        c=int(input("deposite amount"))
        if c<=5000:
            print("amount deposited")
        elif c>=5000:
            print("amount not avilable")
        else:
            print("quit")
    choose2(3)
    def choose3(d):
        d=int(input("change pin"))
        if d!=pin:
            print("change my pin")
        elif d==pin:
            print("pin not changed")
    choose3(4)      
    def choose4(e):
        e=int(input("collect amount"))
        if e<=5000:
            print("collect ammount")
        elif e>=5000:
            print("no chnce to collect u r amount")
        else:
            print("transaction completed successfully")
atm()
				
