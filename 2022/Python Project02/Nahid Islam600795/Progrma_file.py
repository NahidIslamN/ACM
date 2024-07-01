def ADD_DATA():
    ID=input("Enter the ID number : ")
    Name=input("Enter the Name number : ")
    Father_name=input("Enter the Father name number : ")
    Mother_name=input("Enter the Mother Name number : ")
    file=open("Data.txt","a")
    file.write(ID)
    file.write('''
''')
    file.write(Name)
    file.write('''
''')
    file.write(Father_name)
    file.write('''
''')
    file.write(Mother_name)
    file.write('''

''')
    file.close()

#read DaTa form DATA.txt
def Show_Data(a):
    with open("Data.txt")as Datafile:
        line_num=0
        for x in Datafile:
            if x.find(a) !=-1:
                a=line_num
                break
            line_num=line_num+1
    F=open("Data.txt","r")
    x=F.readlines()
    print(x[a])
    print(x[a+1])
    print(x[a+2])
    print(x[a+3])
    F.close()
Show_Data("2021006")
    
        

