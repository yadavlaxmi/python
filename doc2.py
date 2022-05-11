# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

a="w3resource"
b=list(a)
i=0
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
    
        