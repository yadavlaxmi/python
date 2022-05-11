# Question 9

# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.
# Example:-
# Output :-

# {'M':1,'I':4,'S':4,'P':2}

a="MISSISSIPPI"
b=list(a)
i=0
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
    
        
        
    