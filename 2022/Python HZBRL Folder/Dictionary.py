def Show_Data(a):
    print("Name : ",Student[a]["Student Name "])
    print("Student ID : ",Student[a]["Student ID"])
    print("Father Name : ",Student[a]["Father Name"])
    print("Mother Name : ",Student[a]["Mother Name"])
#Dictionary in python#Dictionary in python#Dictionary in python#Dictionary in python

#Create a Dictionary
dictionary_name = {
    "key":"value",
    "key":"value",
    "key":"value",
    }

My_info ={
    "Name : ":"Nahid Islam",
    "Father Name : ":"Md. Jakaria Islam",
    "Mother Name : ":"Mst. Lovely Begum",
    }
My_info.update([("Sister Nmae : ","Jarin Juthi")])
My_info["BF Name :"]="Musfiqur Mahid"

#print(My_info["Mother Name : "])
#print(My_info["Father Name : "])
#print(My_info["Name : "])



#for x in My_info:
#    print(x,My_info[x])

# Add item to a dictionary

My_info["Village : "] = "Palashbary"
My_info["Upozilla : "] = "Birganj"
#for n in My_info:
#    print(n,My_info[n])

My_info.update([("Dictict : ","Dinajpur"),("Country : ","Bangladesh")])
#for x in My_info:
#    pr
Student = {
    "Nahid Islam":{
        "Student Name ":"Nahid Islam",
        "Student ID" : "600795",
        "Father Name":"Md. Jakaria Islam",
        "Mother Name":"Mst Lovely Begum",
        },
    "Mahid Islam":{
        "Student Name ":"Mahid Islam",
        "Student ID" : "600797",
        "Father Name":"Md. Rejaul Karim",
        "Mother Name":"Mst Mukta Begum",
        },
    "Nilima Rani Roy":{
        "Student Name ":"Nilima Rani Roy",
        "Student ID" : "600798",
        "Father Name":"Horen Chandra roy",
        "Mother Name":"Nil Krisna Bewya",
        },
    
    }
for a in Student:
    print("Name : ",Student[a]["Student Name "])
    print("Student ID : ",Student[a]["Student ID"])
    print("Father Name",Student[a]["Father Name"])
    print("Mother Name",Student[a]["Mother Name"])

List=["Nahid Islam","Mahid Islam","Ramjan Ali","Rubel Islam"]
List.append("Rahimul Islam")
List.insert(0,"Musfiqur Mahid")
List.pop()
List.remove("Nahid Islam")
List[1]="Md. Mahid Islam"




for b in List:
    print(b)




#Show_Data(str(input("Enter Student Name : ")))










