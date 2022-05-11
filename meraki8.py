# Question 8

# Take input of name and marks of 10 students and store to a dictionary.
# Output :-

# {
#  'sonu':85,
#  'Kartik':90,
#  'Deepak':96,
#  'Aman':76,
#  'Somesh':60,
#  'Umesh':85,
#  'Amarpal':70,
#  'Roshan':57,
#  'Riyaz':98,
#  'Shabid':56
# }
# # dic={
# # 'sonu':85,
# # 'Kartik':90,
# # 'Deepak':96,
# # 'Aman':76,
# # 'Somesh':60,
# # 'Umesh':85,
# # 'Amarpal':70,
# # 'Roshan':57,
# # 'Riyaz':98,
# # 'Shabid':56
# # }
# # print(dic)

# # (OR)


a=int(input("num"))
b={}
for i in range(a):
    c=(input("keys"))
    d=int(input("values"))
    b.update({c:d})
print(b)

