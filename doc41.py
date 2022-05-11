# Q41.Write a Python program to filter the height and width of students, which are stored in a dictionary. 
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

dic={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
dic1={}
for i in dic:
    k=dic[i]
    j=0
    while j<len(k):
        if k[0]>6 and k[1]<=70:
            key=i
            dic1[key]=(k[0],k[1])
        j+=1
print(dic1)