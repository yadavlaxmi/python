print("enter at least 8 characters")
upper=input("enter at least one upper lettet")
lower=input("at least one lower letter")
number=int(input("at least one number"))
symbol=input("at least one symbol")
if upper>="A" and upper<="Z":
	if lower>="a" and lower<="z":
		if number>=1 and number<=9:
			if symbol in("@","#","$","_","&","-","+","("):
				print(upper+lower+str(number)+symbol)
