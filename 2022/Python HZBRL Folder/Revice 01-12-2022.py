# Worke With Number Datatype in python

A = -20
pi = 3.14161416
#print(type(A))
#print(type(pi))

#Number Mahtouds in python

# Getting the abs value of python
#print(abs(A))
#print(round(pi,2))
#print(pow(abs(A),3))
#print(divmod(abs(A),3))

# Worke With string in python
Nahid = 'Hi I am Nahid. I love "Python" Programing vary Much'
#print(Nahid)

Type01 = '''The quick brown fox jump over the lazy dog. The quick brown fox jump over the lazy dog. The quick brown fox jump over the lazy dog.
The quick brown fox jump over the lazy dog. the qucik brown fox jump over the lazy dog. the quick brown fox jump over the lazy dog. the quick brown fox jump
over the lazy dog. '''
Type02 = '''abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz
abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz'''
Type03= Type01+Type02
#print(Type03)
#print(Type03[302])
#print(Type03[309:])
#print(Type01[3:6])

#String Mathoods

#print(Type01.capitalize())
#print(Type02.upper())
#print(Type03.lower())

#Rep = Type01.replace("dog","Lion")
#print(Rep)


# Work With list in python
Student_List = ["Nahid Islam","Mahid Islam","Roki Islam","Broni Akter", "Sompa Moni"]
Student_List.append("Nandita Sharma")
#print(Student_List)
Student_List[2]= " Md. Rokey Islam"
#print(Student_List)
Student_List.insert(1,"Labib Islam")
Student_List.append("Habib Islam")
#print(Student_List[0:])
Student_List.pop()
#print(Student_List)
Student_List.remove("Nahid Islam")
#print(Student_List)

Student_List[5] = "Nandita Rani Shill"
#print(Student_List)


List01=["Mahid Islam","Akhy Islam", "Rahim Islam","Ratul Rana"]
List02=["Mina Mina","Mostofa Kamal","Bhakti Rani Shill","Nilima Roy"]
List02.extend(List01)
#print(List02[0:6])

#Print Hellow World Using fanction in python

def Nahid():
    print("Hellow World")


def Friends(Name):
    X= "Hellow " + Name
    print(X)



def adding_3_number(a,b,c):
    Sum = a+b+c
    print(Sum)




# Getting the greade from marks
a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B : "))
c = int(input("Enter the value of C : "))
if a>=80 and b>=80 and c>=80 :
    print("A+")
elif a>=70 and b>=70 and c>=70:
    print("A")
elif a>=60 and b>=60 and c>=60:
    print("A-")
elif a>=50 and b>=50 and c>=50:
    print("B")
elif a>=40 and b>=40 and c>=40:
    print("C")
elif a>=33 and b>=33 and c>=33:
    print("D")
else:
    print("Your Are fail")
                
                











