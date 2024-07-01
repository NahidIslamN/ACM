import math
class Numbers:
    def __init__(self,a,b,c):
        self.a=a
        self.b=c
        self.c=c
    def Compare_which_largest(self):
        if self.a>self.b and self.a>self.c:
            print("A is the largest value : ",self.a)
        elif self.b>self.a and self.b>self.c:
            print("B is the largest value : ",self.b)
        else:
            print("C is the largest value : ",self.c)
    def Traingle_Area(self):
        if (self.a+self.b)>self.c and (self.a+self.c)>self.b and (self.c+self.b)>self.a):
            S=(self.a+self.b+self.c)\2
            Traingle_Area=math.sqrt(S*(S+self.a)+(S+self.b)+(S+self.c))
            print(Traingle_Area)
            
