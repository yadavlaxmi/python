# Q6.
# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dic={0: 10, 1: 20}
dic1={}
for i in range(3):
    dic[i]=i*10+10
print(dic)
    
    