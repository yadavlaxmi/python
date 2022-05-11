# Q13.Write a Python program to sum all the items in a dictionary.

my_dict={"data1":10,"data2d":20,"data3":30}
s=0
for i in my_dict:
    s=s+my_dict[i]
print(s)