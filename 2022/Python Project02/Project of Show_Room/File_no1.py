
#Creating an object of a show room by inheratence:
class Wallton:
    def __init__(self,Product_Name,Product_ID,Quality):
        self.Product_Name=Product_Name
        self.Product_ID=Product_ID
        self.Quality=Quality


class Freez(Wallton):
    def __init__(self,Product_Name,Product_ID,Quality,Cetagory,Cost,LT):
        super().__init__(Product_Name,Product_ID,Quality)
        self.Cetagory=Cetagory
        self.Cost=Cost
        self.LT=LT
    def Show_Freez_Details(self):
        print("Product Name : ",self.Product_Name)
        print("Product ID : ",self.Product_ID)
        print("Quality : ",self.Quality)
        print("Cetagory : ",self.Cetagory)
        print("Cost : ",self.Cost)
        print("Low tem : ",self.LT)


class Fan(Wallton):
    def __init__(self,Product_Name,Product_ID,Quality,Cost,Speed):
        super().__init__(Product_Name,Product_ID,Quality)
        self.Cost=Cost
        self.Speed=Speed
    def Show_Fan_Details(self):
        print("Product Name : ",self.Product_Name)
        print("Product ID : ",self.Product_ID)
        print("Quality : ",self.Quality)
        print("Fan Cost",self.Cost)
        print("Fan Speed",self.Speed)

    
class TV(Wallton):
    def __init__(self,Product_Name,Product_ID,Quality,Cost,Color,Hight,Wide):
        super().__init__(Product_Name,Product_ID,Quality)
        self.Cost=Cost
        self.Color=Color
        self.Hight=Hight
        self.Wide=Wide
    def Show_TV_Details(self):
        print("Product Name : ",self.Product_Name)
        print("Product ID : ",self.Product_ID)
        print("Quality : ",self.Quality)
        print("Cost : ",self.Cost)
        print("Color : ",self.Color)
        print("Hight : ",self.Hight)
        print("Wide : ",self.Wide)
#Object creation is finshied and dara accessing is finished by some methods and class


        
        
#Creating a mathods of add data and save them in a txt document      
def Add_Data(b):
    if 5051001 <=b<= 5059999:
        a=input("Enter your porduct Name : ")
        b=str(b)
        c=input("Enter your Freez Quality : ")
        d=input("Enter your Freez Cetagory : ")
        e=input("Enter your Freez Cost : ")
        f=input("Enter your Product Low Temperature : ")
        F=Freez(a,b,c,d,e,f)
        Fi=open("Freez.txt","a")
        Fi.write(b)
        Fi.write('''
''')
        Fi.write(a)
        Fi.write('''
''')
        Fi.write(c)
        Fi.write('''
''')
        Fi.write(d)
        Fi.write('''
''')
        Fi.write(e)
        Fi.write('''
''')
        Fi.write(f)
        Fi.write('''

''')
        Fi.close()
        F.Show_Freez_Details()


    elif 5061001 <=b<=5069999:
        a=input("Enter your porduct Name : ")
        b=str(b)
        c=input("Enter your Fan Quality : ")
        d=input("Enter your Fan Cost : ")
        e=input("Enter your Fan Speed : ")
        F2=Fan(a,b,c,d,e)
        Fi=open("Fan.txt","a")
        Fi.write(b)
        Fi.write('''
''')
        Fi.write(a)
        Fi.write('''
''')
        Fi.write(c)
        Fi.write('''
''')
        Fi.write(d)
        Fi.write('''
''')
        Fi.write(e)
        Fi.write('''

''')
        Fi.close()
        
        F2.Show_Fan_Details()

        
    elif 5071001 <=b<=5079999:
        a=input("Enter your porduct Name : ")
        b=str(b)
        c=input("Enter your Product Quality : ")
        d=input("Enter Your TV Cost : ")
        e=input("Enter Your TV Color :  ")
        f=input("Enter Your TV Hight : ")
        g=input("Enter Your TV Wide : ")
        T=TV(a,b,c,d,e,f,g)
        Fi=open("TV.txt","a")
        Fi.write(b)
        Fi.write('''

''')
        Fi.write(a)
        Fi.write('''
''')
        Fi.write(c)
        Fi.write('''
''')
        Fi.write(d)
        Fi.write('''
''')
        Fi.write(e)
        Fi.write('''
''')
        Fi.write(f)
        Fi.write('''
''')
        Fi.write(g)
        Fi.write('''
''')
        Fi.close()
        T.Show_TV_Details()
    else:
        print("Input a vaild Product ID !")
        
#Add_Data (int(input("Enter your product ID : ")))
# Add data mathods creation is  complete




# Creating a function to accessing Data thorugh product ID From this txt file where I input data 
a=int(input("Enter your Product ID : "))
def Show_Details(x):
    N=str(x)
    if 5051001 <=x<= 5059999:
        with open("Freez.txt","r") as F:
            LN=0
            for i in F:
                if i.find(N) !=-1:
                    M=LN
                    break
                LN+=1
        file=open("Freez.txt","r")
        lines=file.readlines()
        print("Product ID : ",lines[M])
        print("Product Name : ",lines[M+1])
        print("Product Quality : ",lines[M+2])
        print("Product  : ",lines[M+3])
        print("Product Cost : ",lines[M+4])
    elif 5061001 <=x<= 5069999:
        with open("Fan.txt","r") as F:
            LN=0
            for i in F:
                if i.find(N) !=-1:
                    M=LN
                    break
                LN+=1
        file=open("Fan.txt","r")
        lines=file.readlines()
        print("Product ID : ",lines[M])
        print("Product Name : ",lines[M+1])
        print("Product Quality : ",lines[M+2])
        print("Product Cost : ",lines[M+3])
        print("Product Speed: ",lines[M+4])
    elif 5071001 <=x<= 5079999:
        with open("TV.txt","r") as F:
            LN=0
            for i in F:
                if i.find(N) !=-1:
                    M=LN
                    break
                LN+=1
        file=open("TV.txt","r")
        lines=file.readlines()
        print("Product ID : ",lines[M])
        print("Product Name : ",lines[M+1])
        print("Product Quality : ",lines[M+2])
        print("Product Cost : ",lines[M+3])
        print("Product Color : ",lines[M+4])
        print("Product Hight : ",lines[M+5])
        print("Product Wide : ",lines[M+6])

Show_Details(a)
# Finished the mathoods of Show Data by product iD'''

#Creating a function to adite Data from the txt file

           





    




        













    

    

    




    
    
        
