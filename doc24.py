# Q24.
# Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

dic=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
a={}
for x in dic:
    if x not in dic:
        dic[x] = list()
    else:
        a=list()
print(list)
        