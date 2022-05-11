# 40.Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
a=int(input("num"))
b=int(input("num"))
sum=a+b
if sum>15 and sum<20:
	print("20")
else:
	print("not between")