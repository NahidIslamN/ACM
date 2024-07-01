#Assingment operator in python

A= 60
B=2
C = 66
D = 30
A+=C #A=(A+C)
#print(A)
C*=A # C = (C*A)
#print(C)
C-=A # C=(C-A)
#print(C)

D/=B #D=(D/B)
#print(D)
A**=B #A = (A**B)
#print(A)
C//=D #C=(C//D)
#print(C)
C%=D # C= (C%)
#print(C)



List = ["Nahid Islam", "Mahid Islam"]
List[1]="Robi Barman"
#print(List)
List1 = ["Soniya Akter","Runa Akter"]
List.extend(List1)
#print(List)



# Function in python

# Print Hellow world to create a function
def Hellow():
    print("Hellow Pyhton")
Hellow()

def Hellow02(Name):
    X = "Hellow " +Name
    print(X)
Hellow02("Sujon CB")
Hellow02("Nahid Islam")
Hellow02("Mahid Islam")
Hellow02("Rohit Sharma")
Hellow02("Subol Barman")
Hellow02("Md. Nahid Islam")

def add(a,b,c):
    Sum = a+b+c
    print(Sum)
add(10,20,30)

Phone_Number= str(input("Enter yoru Phone Number : "))
if  len(Phone_Number)>11:
    print("Enter a vaild Phone number")
elif Phone_Number[0:3]=="017":
    print('''You are GP user
     Your Phone Number is : ''',Phone_Number)
elif Phone_Number[0:3]=="013":
    print('''You are GP user
     Your Phone Number is : ''',Phone_Number)
elif Phone_Number[0:3]=="018":
    print('''You are Robi User
    Your phone Number is : ''',Phone_Number)
elif Phone_Number[0:3]=="015":
    print('''You are Teletalk User 
    Your phone Number is : ''',Phone_Number)
elif Phone_Number[0:3]=="019":
    print('''You are Banglalink User 
    Your phone Number is : ''',Phone_Number)
else:
    print("Enter a vaild Phone number!!!!!")



















