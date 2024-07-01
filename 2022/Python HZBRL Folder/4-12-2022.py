#Work with dictionary Data type in python================Work with dictionary Data type in python

# Create a dictionary in pythone
def Show_Data(a):
    x = Student_Data["Name "+a]
    y = Student_Data["Father Name "+a]
    z = Student_Data["Mother Name "+a]
    print("Name : ",x)
    print("Father Name : ",y)
    print("Mother Name : ",z)

Student_Data = {
    "Name 600795":"Nahid Islam",
    "Father Name 600795":"Md. Jakaria Islam",
    "Mother Name 600795":"Mst. Lovely Begum",
    "Name 600796":"Mahid Isalm",
    "Father Name 600796":"Regaul Karim",
    "Mother Name 600796":"Mukta Begum"
    }

# Add a new item to a dictionary
Student_Data["Name 600797"]="Nilima Chowdhory"
Student_Data["Father Name 600797"]="Nilondo Ram Babu"
Student_Data["Mother Name 600797"]="Nandita Rani Roy"
#Show_Data(input("Enter your roll : "))
#print("Name : ",Student_Data["Name 600795"])
#print("Father Name : ", Student_Data["Father Name 600795"])
#print("Mother Name : ", Student_Data["Mother Name 600795"])
#Student_Data.pop("Name 600796")
#print(Student_Data)

# Nested Dictionary
# ডিকসোনারির ভিতরে যদি আরো ডিকসোনারি তৈরি করা হয় তবে তাকে নেসট্রেট ডিকসোনারি বলে।
def ShSD(a):
    b =SD[""+a]["Technology"]
    c = SD[""+a]["Roll"]
    d=SD[""+a]["Father Name"]
    e=SD[""+a]["Mother Name"]
    f=SD[""+a]["SSC GPA"]
    print("Technology : ",b)
    print("Roll : ",c)
    print("Father Name : ",d)
    print("Mother Name : ",e)
    print("SSC GPA : ",f)
    
SD = {
    "Nahid Islam":{
        "Technology":"Computer",
        "Roll":"600795",
        "Father Name":"Jakaria Islam",
        "Mother Name":"Lovely Begum",
        "SSC GPA":"4.89"
        },
    "Mahid":{
        "Technology":"Computer",
        "Roll":"600796",
        "Father Name":"Regaoul Karim",
        "Mother Name":"Mukta Begum",
        "SSC GPA":"5.00"
        },
    "Ranu Mondo":{
        "Technology":"Computer",
        "Roll":"600734",
        "Father Name":"Md. Shifat Islam",
        "Mother Name":"Nishat Akter",
        "SSC GPA":"4.89"
        }
    }

ShSD(str(input("Enter Student Name : ")))

# Dictionary



















