class Students:
    def __init__(self,Name,Roll,Department,Session,Institute):
        self.Name=Name
        self.Roll=Roll
        self.Department=Department
        self.Session=Session
        self.Institute=Institute
    def Show_Data(self):
        print("Name : ",self.Name)
        print("Roll : ",self.Roll)
        print("Department : ",self.Department)
        print("Session : ",self.Session)
        print("Institute : ",self.Institute)
Student1=Students("Nahid Islam",600795,"Computer Science and Technology","2021-2022","Thakurgaon Polytechnic Institute")
Student2=Students("Nargis Akter",600757,"Computer Science and Technology","2021-2022","Thakurgaon Polytechnic Institute")
Student3=Students("Nandita Rani Shill",600734,"Computer Science and Technology","2021-2022","Thakurgaon Polytechnic Institute")
print(self.Name)
