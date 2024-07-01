# Bitwise Operator in python.................
# পাইথনে বিটওয়াইজ ওপারেটর বরে বোঝা বিট এবং বাইট অর্থাৎ (0,1) নিয়ে কাজ করা।
#যেমনঃ-

#পাইথনে বিট ওয়াইজ ওপারেটর গুলো প্রথমে কোন সংখ্যার বাইনারি সংখ্যা গুলোকে এন্ড অথবা নট গেইট ;অথবা অন্যান্য ওপারেশন
# করে তার পার রেজালট এর সময় আবার পূর্ণ সংখ্যই আউট পুট দেয়।
#Bitwise and Operator
#Num1=11
#Num2=12
#Num3=Num1 & Num2
#print(Num3)

# Bit wise or Operator.............
Num4=5
Num5=4
#Num6=Num4 | Num5
#print(Num6)

# Bitwise  Xor Operator
Num7 = Num4 ^ Num5
#print(Num7)

# bitwise Nagation (problem)

# Bitwise Left Shift and Bitwise Right Shift
Num8=20
Num9=Num8>>10
#print(Num9)
Num10=Num8<<10
#print(Num10)
a=20480
#print(bin(a))

# Looping Stracture in python
# লুপ অর্থ হলো বার বার করা । পাইথনে বা অন্য কোন ল্যাঙগুয়েজে একই কাজ  বার বার কারার প্রয়োজন হলে লুপ ব্যবহার করা হয়।
#লুপ স্টেমেন্টে একটি কন্ডি শন থাকে যতক্ষণ পর্যন্ত কন্ডিশন ফলস্ না করে ততক্ষণ পর্যন্ত লুপ কাজ করে । আর কন্ডিশন ফলস্ করলেই
#লুপ কাজ করা বন্ধ করে দেয় ।

# While loof in python......

#Syntax
#i=Start value
#while condition:
#    while body/condition code
#     i=i+1 increment/dcrement
#যেমন ঃ -
#a=100
#while a>0:
#    print(a)
#    a=a-1
# For loop in python
#for variable in Sequence:
#    Statements

#Friends=["Nahid Islam","Mahid Islam","Monir Islam","Rayhan Islam","Rohit Islam"]
#for a in Friends:
#    print(a)

#for i in range(0,100,5):
#    if i==50:
#        break
    #print(i)

# 1+2+3+4+5+6.......+n? প্রবলেম সলভ। by while loof
#Sum=0
#n=int(input("Enter the value of  N  : "))
#while n>0:
#    Sum=Sum+n
#    n=n-1
#print("The sum result of number n is ",Sum)

# 1+2+3+4+5.......+100? প্রবলেম সলভ। by for loof
#Sum=0
#for a in range(1,101,1):
#    Sum=Sum+a
#print("The sum result of 100 is : ",Sum)

# কোন সংখ্যার ফেক্টরিয়াল মান বের বারা প্রোগ্রাম।
#Fact=1
#i=int(input("Enter the value of Num : "))
#if i<0:
#    print("Negtive Number is not Allawed")
#elif i==0 or i==1:
#    print("The Factorial number is : 1")
#else:
#    while i>1:
#        Fact=Fact*i
#        i=i-1
#    print("The factorial number is : ",Fact)

# Bottle Problem from (Alamgir Sir)
#Sum=int(input("Enter the Number of Cocacola : "))
#N=int(input("Confrim the Number : "))
#if N<0:
#    print("Worng value!")
#elif Sum != N:
#    print("Wrong value !")
#elif N==1:
#    print("You are abble to Drink : 2")
#elif N==2:
#    print("You are abble to Drink : 3")
#else:
#    while N>2:
#        Sum=Sum+(N/3)
#        N=N//3
#    print("You are abble to Drink :",round(Sum,0)+1)

#List in python..........
# Create a list in python
# Syntax
#List_Name=["Data1","Data2","Data3"]
Family =["Md. Nahid Islam","Md. Jakaria Islam","Mst. Lovely Begum","Mst. Jarin Juthi"]# List in Str
#print(Family[1])
#print(Family[-1])
#print(Family[0:5])

# Adding a Item to a list
Family.append("Ageraddin Islam")
#print(Family[-1])
Family.insert(0,"Reba Khatum")
#print(Family[0])

# Deleting a item to a List
Family.pop()
#print(Family)
Family.remove("Reba Khatum")
#print(Family[0])
#print(len(Family))

a="Reba Khatum" in Family
#print(a)

#List1=[10,20,30,40,80,100] #List in int

#List2=[10.5,20.8,30.3,40.9,80.4,100.5] #List in flot
#List3=["Nahid",20.8,"Mahid",40.9,"Rohit",100.5] #List in misk

#print (List1.sort())


# Dictionary in python

#Create a dictionary
#Syntax
#Dictionary_Name={
#    "Key1":"Value1",
#    "Key2":"Value2",
#    "Key3":"Value3",
#    "Key4":"Value4",
#    "Key5":"Value5",
#    "Key6":"Value6",
#    ..............................
    
#    }

My_info={
    "Name":"Nahid Islam",
    "Father Name":"Md. Jakaria Islam",
    "Mother Name": "Mst Lovely Begum",
    "Institute":"Thakurgaon Polytechnic Institute",
    "Department": "Computer",
    "Roll":"600795",
    }
#print(My_info["Father Name"])
#for a in My_info:
#    print(a,": ",My_info[a])
#My_info.pop("Name")
#My_info.popitem()
#My_info.clear()
#print(My_info)
#My_info["Semester"]="Second"
#print(My_info["Semester"])
My_info.update([("Semester","Second"),("Shift","Frist"),("Group","B(Captin)")])
print(My_info["Group"])












































