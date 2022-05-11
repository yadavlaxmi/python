# Question 5

# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the 2nd list are the corresponding values.
# Example :-
# Input :-

# list1=[“one”,”two”,”three”,”four”,”five”]

# list2=[1,2,3,4,5,]

# Visualize
# Output :-

# {“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
a={}
for i in list1:
    for j in list2:
        a[i]=j
        list2.remove(j)
        break
print(a)