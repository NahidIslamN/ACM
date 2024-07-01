# creating a abstraction method

# at frist your have to diclird a class with inharite ABC calss and define one or more abstractmethods

'''syntax
from abc import ABC,abstractmethod
define a class with inherating ABC calss then define abstractmethod'''

from abc import ABC,abstractmethod

class Sape(ABC):
    
    @abstractmethod
    def Area(self):
        pass

class Ractangle(Sape):
    def __init__(self,h,w):
        self.h=h
        self.w=w
    def Area(self):
        area=self.h*self.w
        return area

class Traingle(Sape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def Area(self):
        area=0.5*self.b*self.h
        return area
class Trapiziam(Sape):
    def __init__(self,w,b,h):
        self.w=w
        self.b=b
        self.h=h
    def Area(self):
        area=0.5*(self.w+self.b)*self.h
        return area


x1=Ractangle(10,30)
x2=Traingle(10,6)
x3=Trapiziam(10,3,5)
print(x2.Area())
    






        
