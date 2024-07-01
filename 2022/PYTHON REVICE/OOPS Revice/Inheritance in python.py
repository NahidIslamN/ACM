# Inheratence in python and many type of  inheratence
class vicale:
    def __init__(self,color,cost):
        self.color=color
        self.cost=cost
    def show_data(self):
        print("I am a vicales. I am",self.color,'''color.
And My cost is ''',self.cost)
class Car1(vicale):
    def __init__(self,color,cost,tyre,glass):
        super().__init__(color,cost)
        self.tyre=tyre
        self.glass=glass
    def show_car(self):
        print("I am a Car. I am",self.color,'''color.
And My cost is ''',self.cost," And I have",self.tyre,"and have",self.glass,"type of glass.")
class Motorcycle(Car1):
        def show_mc(self):
            print("I am a Motorcycle. I am",self.color,'''color.
And My cost is ''',self.cost," And I have",self.tyre,"and have",self.glass,"type of glass.")
class Hallycuptor(vicale):
    def __init__(self,color,cost,fan,computer):
        super().__init__(color,cost)
        self.fan=fan
        self.computer=computer

    def show_hallycuptor(self):
        print("I am a vicales. I am",self.color,'''color.
And My cost is ''',self.cost,"And I have ",self.fan, "and have",self.computer,"too")
    
objv=vicale("Blue","25000 tk")
objc=Car1("Red","6000000 tk",4,3)
objm=Motorcycle("Black","250000 tk",2,1)
objh=Hallycuptor("White","15000000 tk",4,2)
objv.show_data()
objc.show_car()
objm.show_mc()
objh.show_hallycuptor()
objh.show_data()
