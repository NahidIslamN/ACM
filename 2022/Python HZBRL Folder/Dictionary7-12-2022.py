#Dictionary Data type in python-----------Dictionary Data type in python-----------Dictionary Data type in python

#Create a Dictionary

My_Dic = {
    "Name":" Rofique Islam",
    "Blood":"B+ve",
    "Father Name":"Md. Faruk Islam",
    "Mother Name":"Mst. Lovely Begum",
    }
print(My_Dic["Name"])


#Nested Dictionary========Nested Dictionary========Nested Dictionary

#ডিকশনারি ডাটার ভেতর যদি আবার কোন ডিকশনারি দেওয়া হয় েতবে তাকে নেসট্রেট ডিকশনারি বলে।
#Data base project in python

def Shows_Data(roll):
    print("Name : ",SD2[roll]["Name"])
    print("Father Name : ",SD2[roll]["Father Name"])
    print("Mother Name : ",SD2[roll]["Mother Name"])
    print("Roll : ",SD2[roll]["Roll"])
    if (SD2[roll]["Bangla"])>=80 and (SD2[roll]["English"])>=80 and (SD2[roll]["Math"])>=80:
        print("Grade :  A+")
    elif (SD2[roll]["Bangla"])>=70 and (SD2[roll]["English"])>=70 and (SD2[roll]["Math"])>=70:
        print("Grade : A")
    elif (SD2[roll]["Bangla"])>=60 and (SD2[roll]["English"])>=60 and (SD2[roll]["Math"])>=60:
        print("Grade : A-")
    elif (SD2[roll]["Bangla"])>=50 and (SD2[roll]["English"])>=50 and (SD2[roll]["Math"])>=50:
        print("Grade : C")
    elif (SD2[roll]["Bangla"])>=40 and (SD2[roll]["English"])>=40 and (SD2[roll]["Math"])>=40:
        print("Grade : F")
    else:
        print("You are fail in the Exam")
    
    
    

SD2 = {
    "600795":{
        "Name":"Nahid Islam",
        "Father Name":"Md. Jakaria Islam",
        "Mother Name": "Mst Lovely Begum",
        "Roll" : "600795",
        "Bangla": int(60),
        "English":int(80),
        "Math":int(90)},
    "600810":{
        "Name":"Mahid Islam",
        "Father Name":"Rejaul Karim",
        "Mother Name":"Mst Mukta Akter",
        "Roll" : "600810",
        "Bangla": int(90),
        "English":int(95),
        "Math":int(96)},
    "50102":{
        "Name":"Yeamean Islam",
        "Father Name":"Jalal Uddin",
        "Mother Name": "Mst. Nuremadina Begum",
        "Roll" : "600810",
        "Bangla": int(95),
        "English":int(96),
        "Math":int(39)},
    
    }

SD2["600797"]={
        "Name":"Nilima Roy",
        "Father Name":"Krisna Roy",
        "Mother Name": "Lokkhi roy",
        "Roll" : "600810",
        "Bangla": int(70),
        "English":int(100),
        "Math":int(65)
    }
SD2["600803"]={
        "Name":"Sujon Chandra Barman",
        "Father Name":"Sulakkhi Devi",
        "Mother Name": "Horen Chandra Barman",
        "Roll" : "600803",
        "Bangla": int(95),
        "English":int(85),
        "Math":int(90)
    }

#Shows_Data(input("Enter your Roll : "))

    




















