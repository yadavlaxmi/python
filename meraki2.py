# Question 2

# Write a program to print 'exists' if entered key already exists in the dictionary and print 'not exists' if the entered key does not exist.
# Example :-

# dict1={“name”:”Raju”, “marks”:56}

# Visualize
# Note :-

# If input is “name” then output will be “exist”

# If input is “class” then output will be “not exists”.

dict1={
    "name":"raju",
    "marks":56
}
a=(input("char"))
if a in dict1:
    print("exists")
else:
    print("not exists")
    
