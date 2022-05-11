print("hello everyone")
print("_welcome to KBC_")
print("* very good luck for your game***")
print("so lets play the game")
question_list=["what is the capital of India?","How many colours in rainbow?",
"How many girls in navgurukul ? ","which course we are doing in navgurukul?"]
options_list=[["bihar","delhi","kolkata","canada"],["8","9","7","10"],["118","120","100","104"],["beaty palour","swimming course","fashion designer","engineering course"]]
life_line=[["delhi","bihar"],["7","10"],["120","118"],["engineering course","beaty palour"]]
solution_list2=[1,1,2,1]
solution_list=[2,3,1,4]
i=0
count=0
while i<len(question_list):
	print("Q.",i+1,question_list[i])
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1
	user=int(input("choose your option"))
	if user==solution_list[i]:
		print("wao!! congreultion")
	elif user==5050:
		if count==0:
			k=0
			while k<len(life_line[i]):
				print(k+1,life_line[i][k])
				k=k+1
			count=count+1
			user2=int(input("enter any no. "))
			if user2==solution_list2[i]:
				print("you are right")
			else:
				print("wrong:")
				break
		else:
			print("opps! you already used")
			num=int(input("enter any no. "))
			if num==solution_list[i]:
				print("correct")
			else:
				print("opps! srry")
			
	else:
		print("wrong...better luck for the next time")
		break
	i=i+1
	