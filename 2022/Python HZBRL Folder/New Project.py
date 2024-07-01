def Show_Data(a):
    for i in Stu_Data[a]:
        print (i,Stu_Data[a][i])

def Change_Item(a):
        Stu_Data[a]["Name : "]=input("Name : ")
        Stu_Data[a]["Father Name : "]=input("Father Name : ")
        Stu_Data[a]["Mother Name : "]=input("Mother Name : " )
        Stu_Data[a]["Age : "]=input("Age : ")
        
    
Stu_Data={
    "600795":{
        "Name : ":"Nahid Islam",
        "Father Name : ":"Md. Jakaria Islam",
        "Mother Name : ": "Mst. Lovely Begum",
        "Age : ":"17"
        },
    "600796":{
        "Name : ":"Mahid Islam",
        "Father Name : ":"Md. Rejaul Karim",
        "Mother Name : ": "Mst. Mukta Begum",
        "Age : ":"18"
        },
    "600797":{
        "Name : ":"Nandita Sharma",
        "Father Name : ":"Krisna Das",
        "Mother Name : ": "Nirma Roy",
        "Age : ":"16"
        },
    "600798":{
        "Name : ":"Mostafa Anjum Baby",
        "Father Name : ":"Krisna Das",
        "Mother Name : ": "Nirma Roy",
        "Age : ":"16"
        },
     
    }


