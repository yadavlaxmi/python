print("enter at least 8 characters")
upper=(input("enter upper letter"))
lower=(input("lower letter"))
number=int(input("numbers"))
symbol=(input(" symbol"))
if upper>="A" and upper<="Z":
	char1=upper
	if lower>="a" and lower<="z":
		char2=lower
		if number>=0 and number<=9:
			char3=str(number)
			if symbol in("@","#","$","_","&","-","+"):
				char4=symbol
				print(char1+char2+char3+char4)