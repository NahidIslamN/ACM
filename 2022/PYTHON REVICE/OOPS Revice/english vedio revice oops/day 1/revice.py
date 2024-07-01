# init methods in python how to work it full discripthon
'''class Computer:
    def __init__(self,Ram,CPU):
        self.Ram=Ram
        self.CPU=CPU       
    def config(self):
        print(f"The Configure is: Ram is: {self.Ram} and CPU is : {self.CPU}")
com1=Computer("32 GB Ram","i7 10th Gen")
com2=Computer("4 GB Ram","i3 7th Gen")
com1.config()
com2.config()'''

class computer:
    age=80
    def __init__(self):
        self.Name="Nahid Islam"
        self.Roll=600795
        self.Department="CST"
    def update(self):
        self.Name="Fahim Ali"
        self.Roll=600797
        self.Department="Food"
        
obj=computer()

obj2=computer()
computer.update(obj2)
computer.age=18

print(obj2.age)

