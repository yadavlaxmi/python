# Q26.
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# Sample Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11


a= {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in a:
    print(i,end=" ")
print("")
for j in range(len(a)):
    for k in a:
        print(a[k][j],end=" ")
    print()
    
