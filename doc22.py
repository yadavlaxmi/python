# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

dic={'1':['a','b'], '2':['c','d']}
for i in dic["1"]:
    for j in dic["2"]:
        print(i+j)