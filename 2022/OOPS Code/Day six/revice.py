class Parents:
    def __init__(self,Name,Roll,Department):
        self.__Name=Name
        self.__Roll=Roll
        self.__Department=Department
    def Display(self):
        print(self.__Name)
        print(self.__Roll)
        print(self.__Department)
class Child(Parents):
    def Show(self):
        print(self.__Name)
        print(self.__Roll)
        print(self.__Department)
obj=Child("Nahid Islam",600795,"CST")
obj.Display()




        


