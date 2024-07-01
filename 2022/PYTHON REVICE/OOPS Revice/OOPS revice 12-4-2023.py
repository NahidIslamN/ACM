
# create a simple class and object and access the class by this object

'''class Phone:
    def Call(self):
        print("I am making a call")
    def play_game(self):
        print("I am palying a game")
    def massage(self):
        print("I am sending a massage")
x=Phone()
x.Call()
x.play_game()
x.massage()'''


##### createa a object and define tow cetacgory  function one cetagory can set data and one cetagory access Data
'''class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        print("Color : ",self.color)
    def show_cost(self):
        print("Cost : ",self.cost)
x=Phone()
x.set_color("Blue")
x.set_cost("25000 tk")
x.show_color()
x.show_cost()'''

# Create a constraucttor to give data at the time of createing object and define a function to access data
'''class Student:
    def __init__(self,Roll,Name,Father,Mother,Department,Session):
        self.Roll=Roll
        self.Name=Name
        self.Father=Father
        self.Mother=Mother
        self.Department=Department
        self.Session=Session
    def Show_Data(self):
        print("Name : ",self.Name)
        print("Roll : ",self.Roll )
        print("Father Name : ",self.Father)
        print("Mother Name : ",self.Mother)
        print("Department : ",self.Department)
        print("Session : ",self.Session)

s1=Student("600795","Md. Nahid Islam","Md. Zakaria Islam","Mst. Lovely Begum","CST","2021-2022")
s1.Show_Data()'''


# write code with abstraction and polymorphism
'''
from abc import ABC,abstractmethod
class Sape(ABC):
    def show_color(self):
        print("The fill color is Green")
        print("The outline color is Red")

    @abstractmethod
    def Area(self):
        pass
class Traingle(Sape):
    def __init__(self,base,hight):
        self.base=base
        self.hight=hight
    def Area(self):
        area=self.base*self.hight
        print("Area : ",area)
class Rectangle(Sape):
    def __init__(self,hight,wide):
        self.hight=hight
        self.wide=wide
    def Area(self):
        area=(self.hight*self.wide)
        print("Area : ",area)
class Trapiziam(Sape):
    def __init__(self,base1,base2,hight):
        self.base1=base1
        self.base2=base2
        self.hight=hight
    def Area(self):
        area= (self.base1+self.base2) *self.hight*0.5
        print("Area : ",area)

Tra=Traingle(50,25)
Rec=Rectangle(10,20)
Tram=Trapiziam(20,10,3)

Tra.Area()
Rec.Area()
Tram.Area()

Tra.show_color()
Rec.show_color()
Tram.show_color()
'''


    
    
    






              





















    
    
    
