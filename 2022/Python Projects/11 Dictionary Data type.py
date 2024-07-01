# Create a Dictionary========================

#def Show_Data(a):
#    X = Student_Data["Name"+a]
#    Y = Student_Data["Age"+a]
#    Z = Student_Data["Marks"+a]
#    print("Name: ",X)
#    print("Age : ",Y)
#    print("Marks : ",Z)
#def Delete_Data (b):
#    Student_Data.pop("Name"+b)
#    Student_Data.pop("Age"+b)
#    Student_Data.pop("Marks"+b)

#Student_Data = {
#    "Name600795":"Nahid Islam",
#    "Age600795":"17",
#    "Marks600795":"100",
#    "Name600796":"Mahid Islam",
#    "Age600796":"20",
#    "Marks600796":"95",
#    "Name600797":"Mim Akter",
#    "Age600797":"21",
#    "Marks600797":"98",
#    "Name600798":"Roki Islam",
#    "Age600798":"17",
#    "Marks600798":"65",
#    "Name600799":"Nihat Islam",
#    "Age600799":"20",
#    "Marks600799":"65",
#    "Name600800":"Robiul Islam",
#    "Age600800":"55",
#    "Marks600800":"85",
#    "Name600801":"Nandita Rani Shill",
#    "Age600801":"16",
#    "Marks600801":"100",
#    "Name600802":"Evan Islam",
#    "Age600802":"30",
#    "Marks600802":"100",
#    "Name600803":"Rony Islam",
#    "Age600803":"20",
#    "Marks600803":"60",
#    "Name600804":"Monirul Islam",
#    "Age600804":"25",
#    "Marks600804":"95",
#    "Name600805":"Rohit Sharma Ponkojh",
#    "Age600805":"25",
#    "Marks600805":"100" 
#}

#print(type(Student_Data))


#Access Dictionary Data type==========

#print(" Name : ",Student_Data[input("Enter your value : ")])
#print(" Age : ",Student_Data[input("Enter your value : ")])
#print(" Marks : ",Student_Data[input("Enter your value : ")])


# Add Item to a dictionary

#Student_Data["Name600806"]="Mahi Jannat"
#Student_Data["Age600806"]="25"
#Student_Data["Marks600806"]="95"

#Change A Item to Dictionary

#Student_Data["Name600795"]="Md. Nahid Islam"
def Show_Data(a,b):
    X = Employee[a][b]
    if b=="Salery":
        print("Employee Salery :",X)
    else:
        print("Employee Name :",X)
Employee={
    "Exicutive_Director":{
    "Name":"Sujon Chandra Barman",
    "Salery":"500000"
    },
    "Main_Programer":{
    "Name":"Nahid Islam",
    "Salery":"300000"
    },
    "Assestant_Programer":{
    "Name":"Joy Barman",
    "Salery":"150000"
    },
    "Computer_Operator":{
    "Name":"Shipul Kishor",
    "Salery":"20000"
    },
    "Main_Trainer":{
    "Name":"Ambia Khatun",
    "Salery":"20000"
    },
    "Assistant_Trainer":{
    "Name":"Khadija Akter",
    "Salery":"15000"
    }
}
Show_Data(str(input("Enter the Degiknation :")),str(input("Enter the What :")))
#print(Employee["Main_Programer"]["Name"])
#print(Employee["Main_Programer"]["Salery"])






