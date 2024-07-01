class Student:
    def __init__(self,Name,Roll,Department,Session):
        self.Name=Name
        self.Roll=Roll
        self.Department=Department
        self. Session=Session

    def Show_Data(self):
        print("Hi Mr.",self.Name)
        print("Name : ",self.Name)
        print("Roll : ",self.Roll)
        print("Department : ",self. Department)
        print("Session",self.Session)
N=input("Enter your Nmae:")
M=input("Enter your Roll:")
O=input("Enter your Department:")
P=input("Enter your Session:")
S1=Student(N,M,O,P)
S1.Show_Data()

File=open(r"H:\New folder (2)\N.txt","a")
File.write(N)
File.write('''
''')
File.write(M)
File.write('''
''')
File.write(O)
File.write('''
''')
File.write(P)
File.write('''

''')
File.close()






