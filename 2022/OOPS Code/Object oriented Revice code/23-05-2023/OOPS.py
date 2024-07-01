#Parameters constractor
class Email:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a)
        print(self.b)
obj1=Email("nahidislam740405@gmail.com","Thakurgaon")
obj2=Email("mahidislam740405@gmail.com","Dinajpur")
obj3=Email("jahidislam740405@gmail.com","Rangpur")
obj1.display()

class employee:
    def __init__(self):
        self.salary=25000
        self.age=15
e=employee()
e2=employee()
print(e2.__dict__)
