class Man:
    def __init__(self,Name,Roll,Dep):
        self.Name=Name
        self.Roll=Roll
        self.Dep=Dep
    def Show_Details(self):
        print("Congratulation Mr.",self.Name)
        print("Name :",self.Name)
        print("Roll :",self.Roll)
        print("Department : ",self.Dep)
class Woman(Man):
    def Show_Woman(self):
        print("You are a Woman",self.Name)
n=int(input("Enter your Chice with binary number 0 or 1 :"))
if n==0:
    a=input("Enter Your Name : ")
    b=input("Enter Your Roll :")
    c=input("Enter Your Department : ")
    Obj=Woman(a,b,c)
    Obj.Show_Woman()
else:
    if n==1:
        while n==1:          
            a=input("Enter Your Name : ")
            b=input("Enter Your Roll :")
            c=input("Enter Your Department : ")
            Obj=Woman(a,b,c)
            Obj.Show_Details()
            F=open(r"H:\New folder (2)\N.txt","a")
            F.write(a)
            F.write('''
''')
            F.write(b)
            F.write('''
''')
            F.write(c)
            F.write('''

''')
            F.close()
            n=int(input()) 




    

        
    
