# Write a python program by init methods and sotre some data designation programmer fix and company microsoft fix
'''

class Programmer:
    company="Mycrosoft"
    Designation="Programmer"
    def __init__(self,Name,Cuntry,Contact,Gmail):
        self.Name=Name
        self.Cuntry=Cuntry
        self.Contact=Contact
        self.Gmail=Gmail
    def Show_Details(self):
        print("Name : ",self.Name)
        print("Designation : ",self.Designation)
        print("Conpany : ",self.company)
        print("Contact : ",self.Contact)
        print("G-Mail :",self.Gmail)
Programmer1=Programmer("Nahid Islam","Bangladesh","01771139444","nahidislam740405@gmail.com")
Programmer2=Programmer("Alexa","Englend","8565852020","alexax@gmail.com")
Programmer3=Programmer("Jon Doe","Englend","8565852020","alexax@gmail.com")
Programmer4=Programmer("Davite Adom","Englend","8565852020","alexax@gmail.com")
Programmer5=Programmer("Adnan Sharia","India","8565852020","alexax@gmail.com")
Programmer6=Programmer("Adnan Sharia","India","52611","adnans@gmail.com")
Programmer1.Show_Details()


'''




# Write a python program of a clacularor to wich will capable to calculate (+,-,*,/,squer,cube,squreroot)
'''
import math
class Calculator:    
    def Addition(self,a,b):
        self.a=a
        self.b=b
        Ans=(self.a+self.b)
        print(Ans)
    def Minus(self,a,b):
        self.a=a
        self.b=b
                
        if self.a>self.b:
            Ans=self.a-self.b
            print(Ans)
        else:
            Ans=-self.b+self.a
            print(Ans)
    def Maltiplication(self,a,b):
        self.a=a
        self.b=b
        Ans=self.a*self.b
        print(Ans)
    def Devided(self,a,b):
        self.a=a
        self.b=b
        Ans=self.a/self.b
        print(Ans)
    def Pow(self,a,b):
        self.a=a
        self.b=b
        Ans=pow(self.a,self.b)
        print(Ans)

    def Sqrt(self,a):
        self.a=a
        Ans=math.sqrt(self.a)
        print(Ans)
Cal=Calculator()
x=int(input())
y=input("Enter +,-,*,/,p.s to claculate")
if y=="+":
    z=int(input())
    Cal.Addition(x,z)
elif y=="-":
    z=int(input())
    Cal.Minus(x,z)
elif y=="*":
    z=int(input())
    Cal.Maltiplication(x,z)
elif y=="/":
    z=int(input())
    Cal.Devided(x,z)
elif y=="p":
    z=int(input())
    Cal.Pow(x,z)
elif y=="s":
    Cal.Sqrt(x)

'''
# write a python program create a cass and create a atribute and and change after create a object
'''class Simple:
    a="Nahid Islam"
obj=Simple()
obj.a="Mahid Islam"
print(obj.a)
print(Simple.a)
'''

# create a staticmathod to greed the calculator user
'''
import math
class Calculator:    
    def Addition(self,a,b):
        self.a=a
        self.b=b
        Ans=(self.a+self.b)
        print(Ans)
    def Minus(self,a,b):
        self.a=a
        self.b=b                
        if self.a>self.b:
            Ans=self.a-self.b
            print(Ans)
        else:
            Ans=-self.b+self.a
            print(Ans)
    def Maltiplication(self,a,b):
        self.a=a
        self.b=b
        Ans=self.a*self.b
        print(Ans)
    def Devided(self,a,b):
        self.a=a
        self.b=b
        Ans=self.a/self.b
        print(Ans)
    def Pow(self,a,b):
        self.a=a
        self.b=b
        Ans=pow(self.a,self.b)
        print(Ans)

    def Sqrt(self,a):
        self.a=a
        Ans=math.sqrt(self.a)
        print(Ans)

    @staticmethod
    def Greed():
        print("*****Hellow Well come to the best calculator of the world calculate your calculation*****")
Cal=Calculator()
Cal.Greed()

x,y,z=map(str,(input().split()))
x=int(x)
z=int(z)
if y=="+":
    Cal.Addition(x,z)
elif y=="-":
    Cal.Minus(x,z)
elif y=="*":
    Cal.Maltiplication(x,z)
elif y=="/":
    Cal.Devided(x,z)
elif y=="p":
    Cal.Pow(x,z)
elif y=="s":
    Cal.Sqrt(x)
    
'''
# Write a calss train and where can the 3 palse price and sit available, get the train informahtion
class Train:
    Train="Druojan Expraess :1440"
    sit=300
    x=input("Where you Wnat to go: ")

    def Show_Data(self):
        print("Train Name : ",self.Train)
        print("Sit : ",self.sit)
        if self.x=="Dinajpur":
            print("Price is : 90 tk")
        elif self.x=="Pirjanj":
            print("Price is : 30 tk")
        elif self.x=="Rangpur":
            print("Price is : 120 tk")        
   
obj=Train()

obj.Show_Data()


        
        
    











