#Operator in python.....#Operator in python.....#Operator in python.....#Operator in python.....#Operator in python
#Arithmatic Operator(+,-,*,/,//,%,**)
num1 = 50
num2=26
num3=num1%num2
#print(num3)

#Assignment operator in python
#variable_name+=variable_Name

#Comparision Operator
#(>,<,>=,<=,==,!=)

#Logical operator (and or not)
# Bitwise operator


# bitwise operaror

num4=-23
num5=num4 & num3
#print(num5)
num6=num4 | num3
#print(num6)
num7=num4 ^ num3
#print(num7)
a=2
num8 = a<<7
#print(num8)
#print(type(num4))
#print(num4)
#print(abs(num4))
num9=1.141614161416
#print(round(num9,2))
#print(pow(num1,2))
num10=divmod(num1,num2)
#print(num10)

# String Datatype in python................
#single or dubble cotation

text1 = 'Hellow I am Nahid. I am a "python" lover. I love python programing very much'
#print(text1)
text2 = "Hellwo I am Nahid. I am a 'python' lover. I lover python programing very much"
#print(text2)
text3='''The main objective of this syllabus is to provide ample opportunities for the students to use English for variety of
purposes on different situations. Each chepter is vased on theme that contains reading text and a range of tasks an activities
designed to enable the students to practice the different skills, sopmetimes indivcidually and cometimes in pairs or groups.
This syllabus has integrated grammar items into the activities allowing grammar to assume a more meainingful role in learinig
language. thus the student develop their language skills by praciticing language acitvities and not merely knowing the rules of
language'''

#Accing part of string.........

#indexing
#to print a single carecter in of strint data
#print(text3[500])
#print(len(text3))

#   Slycing
#print(text3[195:401])
#print(text1.lower())
#print(text1.capitalize())
#print(text1.upper())
#print(text3.replace("syllabus","Book"))


#List in python

#Create a list......Create a list.....Create a list.....Create a list.....Create a list

Student_List = ["Nahid Islam","Mahid Islam", "Milon Islam","Mohidul Islam","Milon Islam","Rohit Islam"]
#print(Student_List[2])



# Some list mathoos in python.....
#Adding item to a list...................
Student_List.append("Nurnabi Islam")
Student_List.insert(0,"Md. Nahid Ali")

#Deleting item to a list
Student_List.pop()
Student_List.remove("Md. Nahid Ali")



List2=["Jarin Akter","Runa Akter","Sonia Akter","Munni Akter"]
Student_List.extend(List2)
#for a in Student_List:
    #print(a)
#print("Jarin Akter" not in Student_List)
#Function in python
#syntax
#def Function_Name(perameter):
    #Fanction body

# Dictionary in python.......
 #Create a Dictionary

Myinfo= {
    "Name":"Nahid Islam",
    "Department":"Computer",
    "Roll":"600795",
    "Father Name":"Md. Jakaris Islam",
    "Mother Name": "Mst. Loverly Begum",
    }
#print(Myinfo["Father Name"])


# Add item to a dictionary...
Myinfo["Village"]="Palashbary"
Myinfo["Distic"]="Dinajpur"

Myinfo.update([("Desh","Banglsdesh"),("State","Rangpur")])

#Delete item to a dictionary
Myinfo.pop("Desh")
Myinfo.popitem()
Myinfo.clear()
    
for x in Myinfo:
    print(x, ":", Myinfo[x])
    
def Show_Data(a):
    for y in Dict01[a]:
        print(y," : ",Dict01[a][y])

Dict01 = {
    "Nahid Islam":{
        "Name":"Nahid Islam",
        "Father Name":"Md. Jakaria Islam",
        "Mother Name":"Mst. Lovely Begum",
        "Degicnation":"Programer",
        "Selary": "300000"
        },
    "Mahid Islam":{
        "Name":"Mahid Islam",
        "Father Name":"Regaul Karim",
        "Mother Name":"Mukta Begum",
        "Degicnation":"Graphic Designer",
        "Selary": "65000"
        },
    "Km Kajal":{
        "Name":"Km Kajal",
        "Father Name":"Khalek Islam",
        "Mother Name":"Mohima Begum",
        "Degicnation":"Computer Operator",
        "Selary": "30000"
        },
    }
Show_Data(input("Enter your Name : "))
        



    




































