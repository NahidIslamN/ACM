def Show_Data(a):
    X = Student_Data["Name"+a]
    Y = Student_Data["Age"+a]
    Z = Student_Data["Marks"+a]
    print("Name: ",X)
    print("Age : ",Y)
    print("Marks : ",Z)

Student_Data = {
    "Name600795":"Nahid Islam",
    "Age600795":"17",
    "Marks600795":"100",
    "Name600796":"Mahid Islam",
    "Age600796":"20",
    "Marks600796":"95",
    "Name600797":"Mim Akter",
    "Age600797":"21",
    "Marks600797":"98",
    "Name600798":"Roki Islam",
    "Age600798":"17",
    "Marks600798":"65",
    "Name600799":"Nihat Islam",
    "Age600799":"20",
    "Marks600799":"65",
    "Name600800":"Robiul Islam",
    "Age600800":"55",
    "Marks600800":"85",
    "Name600801":"Nandita Rani Shill",
    "Age600801":"16",
    "Marks600801":"100",
    "Name600802":"Evan Islam",
    "Age600802":"30",
    "Marks600802":"100",
    "Name600803":"Rony Islam",
    "Age600803":"20",
    "Marks600803":"60",
    "Name600804":"Monirul Islam",
    "Age600804":"25",
    "Marks600804":"95",
    "Name600805":"Rohit Sharma Ponkojh",
    "Age600805":"25",
    "Marks600805":"100"
        

}

#Show_Data(str(input("Enter your Roll :")))

a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
if a>b and a>c :
    print("The largest value is a : ",a)
elif b>a and b>c:
    print("The largest value is b : ",b)
else:
    print("The largest value is c : ",c)











