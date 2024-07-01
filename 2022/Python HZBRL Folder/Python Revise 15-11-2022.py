#Download Python From (www.python.org) and Install



# Variable And Datatype

Name = ["Nahid Islam", "Mahid Isalm", "Julficar Ali Raju", "Mst. Borny Akter", "Runa Laila" ,"Biplop Sharker", "Bithi Akter"]
#print(Name[2])

print(Nahid[0:])


# Right way to create a variable

Name = "Nahid Islam"
Father_Name = "MD. Jakaria Islam"
Mother_Name = "Mst. Lovely Begum"

#print(Name) ; print(Father_Name) ; print(Mother_Name)
#etc


# Wrong Way to create a variable

# 01 A-Z or a-z and underscore ব্যাতিত অন্য কোন সিম্বল দিয়ে ভেরিয়েবলের নাম শুরু করা যাবে না।
# ভেরিয়েবলের দুইটি শব্দের মাঝখানে কোন প্রকার স্পেস ব্যবহার করা যাবে না।
# কম্পাইলারের keyword কে ভেরিয়েবল হিসাবে ব্যবহার করা যাবে না।


# Datatype------------Datatype------------Datatype------------Datatype------------Datatype------------Datatype------------Datatype------------Datatype

#Number Datatype

#সংখ্যা সমন্ধীয় কোন ডাটা ভেরিয়েবলে স্টোর করা হলে তাকে নাম্বার ডাটা বলা হয়।
#নাম্বার ডাটা টাইপ দুই প্রকার
# 01. Intenger  02. Float
A = 100 #int বা পূর্ণ সংখ্যার ডাটা।
#print(type(A))
B = 300.505 # float বা দশমিক সংখ্যার ডাটা।
#print(type(B))


# String Datatype

# ডাবল বা সিঙ্গেল ব্যারাকেটচ এর ভিতর কোন কিছু লিখলে পাইথনে তা স্ট্রিং ডাটা টাইপ।টেক্স সমন্ধীয় কোন ডাটা ভেরিয়েবলে স্টোর করা হলে তাকে String ডাটা বলা হয়।
Name = "Nahid Islam" # ভেরিয়েবলৈ ডাবল বা সিঙ্গেল কটেশনের মধ্যে কোন ডাটা স্টোর করা হলে তাকে স্ট্রিং ডাটা বলা হয়।
#print(type(Name))


# Boolean Datatype:

# পাইথনে True , False কে Boolean Datatype বলে।
C = True #Boolean Datatype
#print(type(C))
D = False #Boolean Datatype
#print(type(D))


#List Datatype:

# পাইথনে একই ভেরিয়েবলে কো কিছুর তালিকা তৈরি করতে যে ডাটা ব্যবহার করা হয় তাকে লিস্ট ডাটা টাইপ বলে।
Name = ["Nahid Islam", "Mahid Isalm", "Julficar Ali Raju", "Mst. Borny Akter", "Runa Laila" ,"Biplop Sharker", "Bithi Akter"] # List Datatype
#print(type(Name))

# Trupple Datatype পাইথনে সাধারণ ব্যারাকেট এর ভিতর কমা দিয়ে একাধিক ডাটা স্টোর করাকে Trupple Datatype বলে।
#ট্রাপল ডাটা টাইপ একধরণের লিস্ট ডাটা টাইপ শুধু লিস্ট ডাটা টাইপে ডাটা পরিবর্তন করা যায় আর ট্রাপল ডাটা টাইপ পরিবর্তন করা যায় না।


# Set Datatpey

# Dictionary Datatype--------------------------------Dictionary Datatype----------------------Dictionary Datatype
#ডিকশনারি হলে কতগুলে Element  এর সমষ্টি এবং প্রতিটি element একজোড়া key-value এর সংমিশ্রনে গঠিত।




#Opetator --------------Opetator --------------Opetator --------------Opetator --------------Opetator --------------Opetator --------------Operator

#Airthmathic Operator

A = 100
B = 300.505
E = 500
F = 3
G = 20

Addition = A+B # পাইথনে কোন কিছু যোগ করার জন্য “+” চিহ্ন ব্যবহার করতে হয় ।
#print(Addition)
Minus = A-B # পাইথনে কোন কিছু বিয়োগ  করার জন্য “-” চিহ্ন ব্যবহার করতে হয় ।
#print(Minus)
Multiplication = A*B # পাইথনে কোন কিছু গুন  করার জন্য “*” চিহ্ন ব্যবহার করতে হয় ।
#print(Multiplication)
Devided = A/F # পাইথনে কোন কিছু ভাগ  করার জন্য “/” চিহ্ন ব্যবহার করতে হয় ।
#print(Devided)
Devided2 = A//F # পাইথনে কোন কিছু ভাগশেষ ছাড়া ভাগফল বা ইনটেনটার ভাগফর পাওয়ার জন্য  করার জন্য “//” চিহ্ন ব্যবহার করতে হয় ।
#print(Devided2)
Devided3 = A%F # পাইথনে কোন কিছু ভাগশেষ  পাওয়ার জন্য  করার জন্য “%” চিহ্ন ব্যবহার করতে হয় ।
#print(Devided3)
Multiplication2 = A**F  # পাইথনে কোন কিছু উপর পাওয়ারের রেজাল্ট পাওয়ার জন্য  করার জন্য “**” চিহ্ন ব্যবহার করতে হয় ।
#print(Multiplication2)

#Comparition Operator
A = 100
B = 300.505
E = 500
F = 3
G = 20

A>B #Getter then Operator তুলনা করবে A এবং B  এর মধ্যে যদি শর্ত সঠিক হয় তবে বুলিয়ানের True এবং মিথ্যা হলে False Output দিবে।
#print(A>B)
A<B #Less then Operator তুলনা করবে A এবং B  এর মধ্যে যদি শর্ত সঠিক হয় তবে বুলিয়ানের True এবং মিথ্যা হলে False Output দিবে।
#print(A<B)
A>=B
A<=B
A==B
A!=B

#Logical Operator

#Logical "and" Operator
A>=B and A<=B #Logical "and" Operator "and" Operator এর ক্ষেত্রে যদি দুই বা অধিক শর্ত একসাথে কাজ করবে। যদি সবগুলো শর্ত সঠিক হয় তবে Out put True হবে নাহলে False হবে।
#print(A>=B and A<=B)

#Logical "or" Operator
A>=B or A<=B #Logical "or" Operator "or" Operator এর ক্ষেত্রে যদি দুই বা অধিক শর্ত একসাথে কাজ করবে। যদি সবগুলো শর্তর মধ্যে কমপক্ষে একটি শর্ত সঠিক হয় তবে Out put True হবে নাহলে False হবে।
#print(A>=B or A<=B)

#Logical "not" Operator
not (A<B) #Logical "not" Operator "not" Operator এর ক্ষেত্রে যদি শর্ত সঠিক হয় তবে False আর যদি শর্ত মিথ্যা হয় তবে True  হবে।
#print(not (A<B))

#Assingment Operator

A = 100
B = 300.505
E = 500
F = 3
G = 20
A+=E # এটা দ্বারা বুঝায় E এর Value টা A Variable এর মঝে স্টোর করা অর্থৎ (A = A+E)।
#print(A)
F*=A # এটা দ্বারা বুঝায় A এর Value টা F Variable এর মঝে স্টোর করা অর্থৎ (F = A*F)।
#print(F)

#Identify Operator

#Membershift Operator
#Membershift in operator
#কোন ভেরিয়েবলের মাঝে অনেক ডাটা থাকলে কোন নির্দরিষ্ট ডাটা ভেরিয়েবলে আছে কিনা তা জানার জন্য সেই ওপারেটর গুলো ব্যবহার করা হয়।
Name = ["Nahid Islam", "Mahid Isalm", "Julficar Ali Raju", "Mst. Borny Akter", "Runa Laila" ,"Biplop Sharker", "Bithi Akter"]
#print("Nahid Islam"  in Name) # এইখানে বলা হয়েছে Nahid Islam Value টা Name Variable এর মাঝে আছে। যদি থাকে তবে Out put True হবে নাহলে False হবে।
#print("Nahid Islam"  not in Name)  # এইখানে বলা হয়েছে Nahid Islam Value টা Name Variable এর মাঝে ন। যদি  না থাকে তবে Out put True হবে নাহলে False হবে।


#Woke with Number Datatype.........................................Woke with Number Datatype.........................................Woke with Number Datatype

#Getting the type of Number Value......
A = 100 #int Datatype
B = 300.505 #float Datatype
#print(type(A))
#print(type(B))

#Rounding of a float Number
pi = 3.1416182035256
#print(round(pi,2)) #round(যেই ভেরিয়েবল টার দশমিক রিমুভ করবো সেই ভেরিয়েবল,দশমিকের পর কয়টা সংখ্যা থাকবে তার সংখ্যা

#Getting the Abslute Value of a Number
E = -300
F= 300
#print(abs(E)) #abs Mathood এর ভিতর যেই ভেরিয়েবলই দেওয়া হোক না কেন তার প্রজেটিভ ভ্যালু প্রিন্ট করবে।
#print(abs(F))

#Getting devided an riminder/ভাগফল বা ভাগশেষ একসাথে পাওয়ার ফরমুলা ।
A = 100
B = 300.505
E = 500
F = 3
G = 20
I = (divmod(A,F)) #divmod ফরমুলার ভিতর দুইটি ভেরিয়েবল থাকে প্রথম ভেরেয়েবল দ্বারা দ্বিতীয় ভেরিয়েবলকে ভাগ করা হয়েএবং Output হিসাবে ভাগফল এবং ভাগশেষ একসাথে প্রদান করা হয়।
#print(I)

#Getting the superscript Result
#print(pow(A,2)) #pow ফরমুলা দুইটি ভেরিয়েবলের মধ্যে পাওয়ার দেওয়ার কাজ করে েএবং বর্গ সম্বন্ধীয় কার  করে।


#Work With String in Python............................................Work With String in Python............................................Work With String in Python

#Cotation 
S = ' Hi I am Nahid. I a Student of Thakurgaon Politechnic Institute. I love "Python programing" Very much.'
#print(S)

#Multiline String in python........
Speach = '''The quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog.
The quick brown fox jump over the lay dog. the quick brown fox jump over the lay dog. The quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog.
The quick brown fox jump over the lay dog. the quick brown fox jump over the lay dog. The quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog.
The quick brown fox jump over the lay dog. the quick brown fox jump over the lay dog. The quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog.
The quick brown fox jump over the lay dog. the quick brown fox jump over the lay dog. '''
#print(Speach)

#Concaniting String in python........
Speach02 = '''Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz
Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz
Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz
Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz Abcdefghijklmnopqrstuvwxyz '''
#print(Speach+Speach02)

#Accessing Part in Python
#induxing সিঙ্গেল ক্যারাকটার অ্যাকসেস করার জন্য ইন্টিক্সিং করা হয়।
# print(Speach[30])
#Slysing :অনেগুলো  ক্যারাকটার অ্যাকসেস করার  জন্য স্লাইসিং নিয়ে কাজ করা হয়।
# print(Speach[30:])


#Some String Mathoods.......................

#Case Changes in pytghon..........................
#print(Speach.upper())
#print(Speach.capitalize())
#print(Speach.lower())

#Getting the length in python...........
#print(len(Speach))

#Replace A value in pyhon...............................
SpeachN = Speach.replace("dog","Lion")
#print(SpeachN)

#Work With List in python........................Work With List in python........................Work With List in python........................Work With List in python

#Create a List in python.
Student_List = ["Mahid Islam", "Labib Islam","Simla Akter","Sumona Akter"]
#print(Student_List)
#print(Student_List[0:2])


#Add a New Item to a list..................
Student_List.append("Nurnabi")
#print(Student_List)
Student_List.insert(0,"Akash Akash")
#print(Student_List)

#Delete Item from a List...........
Student_List.pop(3)
#print(Student_List)
Student_List.remove("Nurnabi")
#print(Student_List)

#Worke With trupple in python--------------------Worke With trupple in python--------------------Worke With trupple in python

Names= ("Nahid Islam","Mahid Islam","Labib Islam", " Monir islam","Robiul Islam")
#print(type(Names))
print(Names[0:4])
#Worke With trupple in python--------------------
#ট্রাপল লিস্টের মতো একটি ডাটা টাইপ যা  লিস্টের মতো পরিবর্তন করা যায় না।
#ততো বেশি ‍এক্সেস করা যায় না।


# Worke with function in python---------Worke with function in python---------Worke with function in python

# Syntax
#def function_name(perameter):
    #Statements

#Print Hellow World by create a function
def Hellow():
    print("Hellow Word")

Hellow()
Hellow()


#function parameter and arguments
def Hell(Name):
    X = "Hellow " + Name
    print(X)
Hell("Nahid Islam")
Hell("Akhy Islam")

#Program to print addition two number using function
def add(a,b):
    Sum = a+b
    print("Your addition value is : ",Sum)
add(10,20)
add(20,30)

        

















