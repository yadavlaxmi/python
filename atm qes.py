print("wel come to atm")
print("insert atm")
pin=int(input("enter 4 digit pin number"))
amt=5000
if pin==2000:
	print("1.balance enquiry")
	print("2.amount withdraw")
	print("3.amount deposit")
	print("4.change the pin")
	print("5.collect amount")
	print("6.quit")
	choose=int(input("choose transaction"))
	if choose==3:
		a=int(input("amount deposit"))
		if a<=5000:
			print("amount avaliable")
		elif a>=5000:
			print("amount not avaliable")
		else:
			print("quit")
	elif choose==1:
		b=int(input("balance enquiry"))
		if b<=5000:
			print("valid balance")	
		elif b>=5000:
			print("balance not avaliable")
		else:
			print("transaction completed")
	elif choose==2:
		c=int(input("amount withdraw"))
		if c>=5000:
			print("please take your amount")
		elif c<=5000:
			print("sorry balance not avaliable")
		else:
			print("thank you")
	elif choose==4:
		d=int(input("change pin"))
		if d != pin:
			print("pin changed")
		elif d== pin:
			print("pin not changed")
	elif choose==5:
		e=int(input("collect amount"))
		if e<=5000:
			print("collect ur amount")
		elif e>=5000:
			print("no chance to collect")
		else:
			print("transaction completed")

