# Create some conductor to receve the atribute at the time of creating the object:


# Createing the class
class Students:
    # The methods should create a conductor for atribute of the calss and take the atribute at the time of creating object
    '''syntax
    def __init__(self,atribute1,atribute,..........atirbute n)
        self.atribute1=atribute1
        self.atribute2=atirbute2
        all atribute shoule be run as such way to acceess the popert wich is given user'''
    def __init__(self,Name,Roll,Dep,Session):
        self.Name=Name
        self.Roll=Roll
        self.Dep=Dep
        self.Session=Session

# I am defineing the methods to access the data and showing the data
    def Show_Details(self):
        print("Name : ",self.Name)
        print("Roll : ",self.Name)
        print("Department : ",self.Dep)
        print("Session : ",self.Session)


# Creating the object of the Students Calss
S1=Students("Nahid Islam","600795","CST","2021-2022")
S1.Show_Details()
        
        

        
