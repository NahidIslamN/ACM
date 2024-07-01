#Number Data type in python

#পাইথনে দুই ধরণের নাম্বার ডাটা টাইপ আছে।
# 1. Intenger পূর্ণ সংখ্যা ডাটা
# 1. Float Datatype দশমিক সংখ্যার ডাটা
#Getting the type of a variable
num1 = 25025
num2 = 25.000
#print(type(num1))
#print(type(num2))
num3=(num2-num1)
#print(abs(num3))
num4=3.14163852565
#print(round(num4,4))
num5 = 250
num6=pow(num5,2)
#print(num6)
num7 = divmod(num1,num5)
#print(num7)

#String Data type in python
# Single or Duble Cotation in python

N = 'Hi I am Nahid Islam. I love "Python" Program very much'
N2="Hi I am Nahid Islam. I love 'Python' Program very much"

#print(N,N2+)

#Multiline String in python
N3='''The quick brown fox jump over the lazy dog. The quick brown fox jump over the lazy do. The quick brown fox jump over the lazy dog.
The quick brown fox jump over the lazy dog. The quick brown fox jump over the lazy dog. The quck brown fox jump over
the lazy dog.'''
#print(N3)
N4 = '''Abcdefghijklmnopqrstuvwxyz. Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqustuvwxyz
Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz
Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz
Abcdefghijklmnopqrstuvwxyz '''

N5 = N4+N3
#print(N5)

#Accessing part of String
#indexing শুধু মাত্র একটি সিঙ্গেল ক্যেরেক্টার প্রিন্ট করার জন্য ইন্ডেক্সিং ব্যবহার করা হয় যেমন:-
#print(N4[25])

#Slysing একসাথে অনেকগুলো ক্যারেক্টার প্রিন্ট করার জন্য স্লাইসিং ব্যবহার করা হয় যেমন:-
#print(N4[0:26])

# String Mathoods

#Convert Upper Case
N5 = N4.upper()
#print(N5)

#Convert Capitalize Case

N6=N4.capitalize()
#print(N6)

N7=N4.lower()
#print(N7)

#print(len(N3))
#print(N3[280])

#Back Slysing
#print(N3[ ::-1])
N8=N3.replace("quick","Slow")
#print(N8)

#List in python

#Create a list
My_Friends = ["Mahid Islam","Mubtashil Islam Labib","Payel Islam","Md. Soheb Islam","Md. Rayhan Islam","Suborna Akter"
              ,"Runa Akter","Sonia Akter","Mostafa Anjum Baby","Akhi Akter","Samsunnahar Mina","Mst. Ranu Akter"]
#print(type(My_Friends))
for o in My_Friends:
    print(o)


# Accessing Part of python
#print(My_Friends[7])
#print(My_Friends[6])
#print(My_Friends[4:])
#print(My_Friends[::-1])

# Adding Item to A list
My_Friends.append("Nilima Rani Roy")
#print(My_Friends[-1])
My_Friends.insert(0,"Rayhan Roni")
#print(My_Friends[0])
My_Friends.pop()
#print(My_Friends)
My_Friends.remove("Rayhan Roni")
#print(My_Friends)
My_Friends[-1]="Ranu Akter"
#print(My_Friends)
#print("Mahid Islam" in My_Friends)
#print("Riad Islam" in My_Friends)
#print("Mahid Islam" not in My_Friends)
#print("Riad Islam" not in My_Friends)
#for a in My_Friends:
#    print(a)

# Function in python
#Syntax:
#    def Function_Name(perameter):
#        Function body

def Show_Friends(a):
    print(My_Friends[a])


My_Friends = ["Mahid Islam","Mubtashil Islam Labib","Payel Islam","Md. Soheb Islam","Md. Rayhan Islam","Suborna Akter"
              ,"Runa Akter","Sonia Akter","Mostafa Anjum Baby","Akhi Akter","Samsunnahar Mina","Mst. Ranu Akter"]


#Show_Friends(int(input("Enter Your Friends Sirial number : ")))

#Dictionary in python
# Create a Dictionary
#Syntax:
#    Dictionary_Name={
#        "Key":"Value",
#        "Key":"Value",
#        "Key":"Value",
        
#        }

#Accing Dictionary my Function
def Show_Data(a):
    print(Mydict[a])

Mydict = {
    "Name":"Nahid Islam",
    "Roll":"600795",
    "Department":"CSE",
    "Father Name":"Md. Jakaria Islam",
    "Mother Name":"Mst. Lovely Begum",
    "Best Friends":"Mostafa Anjum Baby",
    "Girl Friends" : "N/A",
    "Love With":"Mst ................ Akter",
    "Kalima":"La ilaha illalaha muhamadur rasulullah",
    
    }

# Accessing part in python
#print("My BF : ",Mydict["Best Friends"])

# Add item to a dictionary
Mydict["Rob"]="Allah"
#print(Mydict["Rob"])
Mydict.update([("Rasul","Muhammad (S)"),("Din","Islam")])
#print(Mydict["Din"])
#Show_Data(str(input("Enter your Key : ")))

#Delete item from to a dictionary
Mydict.pop("Girl Friends")
Mydict.popitem()
#print(Mydict)
Mydict.clear()
#print(Mydict)
del Mydict
print(Mydict)
            
















