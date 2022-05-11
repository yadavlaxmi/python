# login_signup

import json
import os
dict={}
list=[]
dict1={}
dict2={}
if os.path.exists("userdetails.json"):
    pass
else:
    create=open("userdetails.json","w+")
    create.close()
choose = int(input("choose 1. for sign up or 2. for log in:"))
if choose == 1:
    print("sign up")
    name=input("Enter your name:")
    print(name)
    password=input("Enter your password (password should conatain Upper,Small Letter, Special Character and number):")
    upper,digit,lower,special_char=0,0,0,0
    for i in password:
        if (i.isupper()):
            upper+=1
        if (i.isdigit()):
            digit+=1
        if (i.islower()):
            lower+=1
        if(i=='@'or i=='$' or i=='_' or i=='#'):
            special_char+=1
    try:
        with open("userdetails.json","r") as output:
            user_data=json.load(output)
            for info in user_data["user"]:
                pass
    except:
        pass
    if (lower>=1 and upper>=1 and special_char>=1 and digit>=1 and lower+special_char+upper+digit==len(password)):
        password1=input("confirm password:")
        if password==password1: 
            if  os.stat("userdetails.json").st_size==0:
                date_of_birth=input("Enter Your Date Of Birth:")
                Gender=input("Enter your Gender:")
                print("Congracts",name,"You are signed up Succesfully")

                try:
                    dict2["d_o_b"]=date_of_birth
                    dict2["Gender"]=Gender
                    dict1["Username"]=name
                    dict1["Password"]=password
                    dict1["Profile"]=dict2
                    list.append(dict1)
                    dict["user"]=list
                    with open("demo.json","r+") as file:
                        read_file= file.read()
                        userdata=json.loads(read_file)
                        for i in userdata:
                            if i =="user":
                                a=userdata[i]
                                a.append(dict1.copy())
                                dict["user"]=a
                                json.dumps(dict,file)
                                file.close()
                except:
                    with open("userdetails.json","w") as f:
                        f.write(json.dumps(dict, indent=4))
            else:
                if info["Username"]!= name  or info["Password"]!= password:
                    birth_date=input("Enter Your Date Of Birth:")
                    Gender=input("Enter your Gender:")
                    print("Congracts",name,"You are signed up Succesfully")
 
                    try:
                        dict2["d_o_b"]=birth_date
                        dict2["Gender"]=Gender
                        dict1["Username"]=name
                        dict1["Password"]=password
                        dict1["Profile"]=dict2
                        list.append(dict1)
                        dict["user"]=list
                        with open("userdetails.json","r+") as file:
                            read_file= file.read()
                            userdata=json.loads(read_file)
                            for i in userdata:
                                if i =="user":
                                    a=userdata[i]
                                    a.append(dict1.copy())
                                    dict["user"]=a
                                    json.dumps(dict,file)
                                    file.close()
                    except:
                        with open("userdetails.json","w") as f:
                            f.write(json.dumps(dict, indent=4))
                else:
                    print("Your already Exsist!")
        else:
            print("both password are not matched")
    else:
        print("At least password should contain one upper and lower letter one Specail number or one digit")

elif choose==2:
    print("login")
    your_name=input("Enter your username:")
    your_password=input("Enter your Log in Password:")
    with open("userdetails.json","r") as log_in_file:
        file1=json.load(log_in_file)
        for output_data in file1["user"]:
            if output_data["Username"] == your_name and output_data["Password"]==your_password:
                print("Username",":",output_data["Username"])
                print("Gender",":",output_data["Profile"]["Gender"])
                print("Dob",":",output_data["Profile"]["d_o_b"])
                print(your_name+ "You Logged In Succesfully")
                break
        else:
            print("incorrect details")
