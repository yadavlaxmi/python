# Q8.Tumhare pass four employes ki details hai list mai:-

# [“neelam”,”programer”,”24”,”2400”,]
# [“komal”,”trainer”,”24”,”20000”]
# [“anuradha”,”HR”,”25”,”40000”]
# [“Abhishek”,”manager”,”29”,”63000”]
# Visualize
# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
# har ek employee ka dictionary main name,designation,age and salary honi chahiye.
# aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.

# Output:-

# { 
#      "emp1":{ "name":"nilam",
#        "Designation":"programmer",
#        "Age":"34",
#        "salary":"24000",
#          }

#     "emp2":
#       { "name":"komal",
#         "Designation":"Trainee",
#         "Age":"24",
#         "salary":"20000" ,
#         }

 
#     "emp3":
#        { "name":"anuradha",
#          "Designation":"HR",
#          "Age":"25",
#          "salary":"40000",
#          }


#     "emp4":
#        { "name":"Abhishek",
#          "Designation":"Manager",
#          "Age":"29",
#        }
#  }


import json
dic1=["neelam","programer","24","2400"]
dic2=["komal","trainer","24","20000"]
dic3=["anuradha","HR","25","40000"]
dic4=["Abhishek","manager","29","63000"]
list1=[]
list2=[]
list3=[]
list4=[]
dict1={}
dict2={}
dict3={}
dict4={}
a={}
i=0
while i<len(list1):
    var=list4[i]
    dic1[var]=list1[i]
    dic2[var]=list2[i]
    dic3[var]=list3[i]
    dic4[var]=list4[i]
    i+=1
a["emp1"]=dic1
a["emp2"]=dic2
a["emp3"]=dic3
a["emp4"]=dic4
print(a)