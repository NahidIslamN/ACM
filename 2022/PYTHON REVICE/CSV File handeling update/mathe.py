'''from csv import writer,reader,DictWriter,DictReader
class StudentData:
    Collage='Thakurgaon Polytechnic Institute'
    def add_data(self):
        x=input("Enter Your Student ID :")
        a=input("Enter Your Name :")
        b=input("Enter Your Father Name :")
        c=input("Enter Your Mother Name :")
        d=input("Enter Your Roll :")
        e=input("Enter Your Department :")
        head=("Student ID","Name","Father Name","Mother Name","Roll","Department")
        Data=(x,a,b,c,d,e)
        with open('.\Student_DBMS.csv', 'a') as file:
            Writer=writer(file,lineterminator='\n')
            Writer.writerow(Data)
    def show_data(self):
        with open('.\Student_DBMS.csv', 'r') as file:
            Reader=reader(file)
            a=input("Enter SID")
            for row in Reader:
                if row[0]==a:
                    for x in row:
                        print(x)
                    
SDBMS=StudentData()
SDBMS.add_data()
with open('.\Student_DBMS.csv', 'r') as file:
    head=("Student ID","Name","Father Name","Mother Name","Roll","Department")
    Reader=DictReader(file,fieldnames=head,lineterminator='\n')
    Read=list(Reader)
with open('.\Student_DBMS.csv', 'w') as file:
    head=("Student ID","Name","Father Name","Mother Name","Roll","Department")
    Writer=DictWriter(file,fieldnames=head,lineterminator='\n')
    Writer.writeheader()
    for x in Read:
        if x["Student ID"]=="600797":
            x["Mother Name"]="Nilufa Benargy"
        Writer.writerow(x)'''
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
        

