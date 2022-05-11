# 1.average of dictionery:

# dic={"a":23,"b":{"c":28,"d":45}}
# sum=0
# c=0
# for i in dic:
#     if type (dic[i])==type({}):
#         for j in dic[i]:
#             sum+=dic[i][j]
#             c+=1
#     else:
#         sum=sum+dic[i]
#         c+=1
# print(sum/c)


# "my name is swathi my age 20 years old"


# dic="my name is swathi my age 20 years old"
# a=input("enter any char")
# d1=dic.split()
# j=0
# c=0
# dic1={}
# while j<len(d1):
#     if d1[j]==a:
#         c+=1
#     j+=1
#     dic1[a]=c
# print(dic1)

# reverse keys and values:

# dic={1:23,4:25,6:27}
# d={}
# for i in dic:
#     d[dic[i]]=i
# print(d)

# singel dictionary converted into multiple dictionary:

# dic={"a":23,"b":2,"c":28,"d":45}
# dic1={}
# for i in dic:
#     dic1[i]=dic
# print(dic1)

# #two dictionaries converted into singel dictionary:


# dic={"a":23,"b":2,"c":28,"d":45}
# dic1={1:2,3:5,4:8,6:5}
# dic2={}
# for i in dic:
#     dic2[i]=dic[i]
# for j in dic1:
#     dic2[j]=dic1[j]
# print(dic2)


# a={'data':{
#     'jan':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'feb':{'mon':5,'tues':5,'wed':4,'thurs':7,'fri':2,'sat':3,'sun':7},
#     'march':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'april':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'may':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'june':{'mon':2,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'july':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'aug':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'sep':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'oct':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'nov':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'dec':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4}}
# }
# sum=0
# sum=0
# for i in a["data"]:
# 	print("values:",a["data"][i]["mon"])
# for i in a.values():
#     for j in i.values():
#         for k in  j.values():
#             sum=sum+k
#             if k>=4:
#                 print("greater than 4:",k)
# print("total sum:",sum)
    



# # even numbers in dictionary:

# dic={"a":[1,4,7,8,9],"b":[7,4,9,2,3],"c":[5,7,6,8,9,2,4]}
# for i in dic:
#     d={}
#     k=dic[i]
#     empty=[]
#     for j in k:
#         if j%2==0:
#             empty.appennad(j)
#         d[i]=empty
# print(d)

# odd numbers in dictiory:

# dic={"a":[1,4,7,8,9],"b":[7,4,9,2,3],"c":[5,7,6,8,9,2,4]}
# for i in dic:
#     d={}
#     k=dic[i]
#     empty=[]
#     for j in k:
#         if j%2!=0:
#             empty.append(j)
#         d[i]=empty
# print(d)

# # # sum of values:

# dic={"a":2,"b":3,"c":1}
# sum=0
# for i in dic:
#     sum=sum+dic[i]
# print(sum)


# dic1=[1,2,3,4]
# dic2=[10,20,30,40]

# dic3={}
# for i in dic1:
#     for j in dic2:
#         dic3[i]=j
#         dic2.remove(j)
#         break
# print(dic3)


# # count how many float values are there in dictionary

# d={"a":42,"b":12,"c":5.2,"e":30.2,"d":5.2}
# c=0
# for i in d.values():
# 	if type(i)==float:
# 		c+=1
# print(c)
    
    
# # count how many spaces are there in given dictionary

# dict={1:"abc dc",2:"a bcd",3:"ab cd"}
# count=0
# for i in dict:
# 	for j in dict[i]:	
# 		if j==' ':
# 			count+=1
# print('total space:',count)


# # dict={'a':24,'b':12,'c':4}
# # dict1={'f':0.5,'m':4,'a':10,'b':2}
# # output sholud be {"a":34,"b":14}


# dict={'a':24,'b':12,'c':4} 
# dict1={'f':0.5,'m':4,'a':10,'b':2}
# dict2={}
# for i in dict:
# 	for j in dict1:
# 		if i in dict1:
# 			dict2[i]=dict1[i]+dict[i]
# 		elif i in dict2:
# 			dict2[i]=dict1[i]
# print(dict2)


# # count how many srting values are there in given dictionary

# d={"a":42,"b":12,"c":5.2,"e":30.2,"d":"5.2"}
# c=0
# for i in d.values():
# 	if type(i)==str:
# 		c+=1
# print(c)

# # find the minimum value in dictionary

# d={"a":42,"b":12,"c":5.2,"e":30.2,"d":5.2}
# a=list(d.values())
# min=a[0]
# for i in a:
#     if i<min:
#         min=i
# print("min",min)


# # replace the keys in dictionary

# dict={"a":46,"b":52,"c":32}
# dic={}
# c=0
# for i in dict.values():
# 	c+=1
# 	dic[c]=i
# print(dic)

# # print maximum float in this dictionary

# dict1={'a':24,'b':53.6,'c':24.2,'d':12,'e':5.2}
# l=list(dict1.values( ))
# i=0
# max=0
# while i<len(l):
# 	if l[i]>max:
# 		max=l[i]
# 	i+=1
# print(max)


# # remove the spaces in dictionary

# dict={1:"abc dc",2:"a bcd",3:"ab cd"}
# i=0
# space=[ ]
# for i in dict:
# 	j=0
# 	st=' '
# 	while j<len(dict[i]):
# 		if dict[i][j]!=' ':
# 			st+=dict[i][j]
# 		j+=1
# 	space.append(st)
# 	i+=1
# print(space)


# # str="hima"
# # output should be{'h': 'hima', 'i': 'hima', 'm': 'hima', 'a': 'hima'} 


str="hima"
d={}
for i in str:
    d[i]=str
print(d)


# list=[1,2,3,4,5,6,7,8,9,10]
# i=0
# list1=[]
# while i<len(list)-1:
#     j=0
#     list2=[]
#     while j<len(list):
#         list2.append(list[i])
#         i=+1
#         if j==2:
#             break
#         j+=1
#     list1.append(list2)
# a=0
# b={}
# while a<len(list1[i]):
#     b.update({"c1":list1[0]})
#     b.update({"c2":list1[1]})
#     b.update({"c3":list1[2]})
#     b.update({"c4":list1[3]})
#     a+=1
# print(b)
