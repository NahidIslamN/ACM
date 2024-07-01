from csv import reader,writer,DictReader, DictWriter
from tkinter import *
class DelData:  
    def __init__(self,m,n,o,p,q,r,s):
        self.m=m
        self.n=n
        self.o=o
        self.p=p
        self.q=q
        self.r=r
        self.s=s

    def Adite_Data(self):
        if self.q=="1st":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C1.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C1.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
        elif self.q=="2nd":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C2.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C2.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
        elif self.q=="3rd":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C3.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C3.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
        elif self.q=="4th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C4.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C4.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
        elif self.q=="5th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C5.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C5.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
        elif self.q=="6th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C6.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C6.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
        elif self.q=="7th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C7.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C7.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
        elif self.q=="8th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            with open('Data files\Computer\C8.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                Data=Reader=list(Reader)
            with open('Data files\Computer\C8.csv','w') as file:
                Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                for row in Data:
                    if row["Student ID"]==self.m:
                        row["Student Name"]=self.n
                        row["Department"]=self.o
                        row["Session"]=self.p
                        row["Semester"]=self.q
                        row["Shift"]=self.r
                        row["Group"]=self.s
                    Writer.writerow(row)
def edite():
    m=Student_ID.get()
    n=Student_Name.get()
    o=Department.get()
    p=Session.get()
    q=Semester.get()
    r=Shift.get()
    s=Group.get()
    x = DelData(m,n,o,p,q,r,s)

    x.Adite_Data()

def clears():
    DataEntry1.delete(0, END)
    DataEntry2.delete(0, END)
    DataEntry3.delete(0, END)
    DataEntry4.delete(0, END)
    DataEntry5.delete(0, END)
    DataEntry6.delete(0, END)
    DataEntry7.delete(0, END)
    DataEntry8.delete(0, END)
    DataEntry9.delete(0, END)

root3 = Tk()
root3.title("Data Entry Form")
root3.configure(background="#636e72")
root3.geometry("650x600")
root3.resizable(0, 0)

text1 = Label(root3, text="Student Data Form", fg="white", bg="red")
text1.pack(pady=(10, 10), fill="both")
text1.config(font=("impact", 30))

# Student_ID, Student_Name, Department, Session, Semester, Shift, Group

Data1 = Label(root3, text="Student ID", font="20", fg="white", bg="#636e72").place(x=50, y=150)
Data2 = Label(root3, text="Student Name", font="20", fg="white", bg="#636e72").place(x=50, y=200)
Data3 = Label(root3, text="Department", font="20", fg="white", bg="#636e72").place(x=50, y=250)
Data4 = Label(root3, text="Session", font="20", fg="white", bg="#636e72").place(x=50, y=300)
Data5 = Label(root3, text="Semester", font="20", fg="white", bg="#636e72").place(x=50, y=350)
Data6 = Label(root3, text="Shift", font="20", fg="white", bg="#636e72").place(x=50, y=400)
Data7 = Label(root3, text="Group", font="20", fg="white", bg="#636e72").place(x=50, y=450)

# entry
Student_ID = StringVar()
Student_Name = StringVar()
Department = StringVar()
Session = StringVar()
Semester= StringVar()
Shift = StringVar()
Group = StringVar()
ID = StringVar()
Sem = StringVar()

DataEntry1 = Entry(root3, width=40, textvariable=Student_ID)
DataEntry1.place(x=190, y=150)
DataEntry2 = Entry(root3, width=40, textvariable=Student_Name)
DataEntry2.place(x=190, y=200)
DataEntry3 = Entry(root3, width=40, textvariable=Department)
DataEntry3.place(x=190, y=250)
DataEntry4 = Entry(root3, width=40, textvariable=Session)
DataEntry4.place(x=190, y=300)
DataEntry5 = Entry(root3, width=40, textvariable=Semester)
DataEntry5.place(x=190, y=350)
DataEntry6 = Entry(root3, width=40, textvariable=Shift)
DataEntry6.place(x=190, y=400)
DataEntry7 = Entry(root3, width=40, textvariable=Group)
DataEntry7.place(x=190, y=450)

IDLabel = Label(root3, text="Student ID", font="20", fg="white", bg="#636e72").place(x=500, y=250)
DataEntry8 = Entry(root3, width=20, textvariable=ID)
DataEntry8.place(x=500, y=280)

SemLabel = Label(root3, text="Semester", font="20", fg="white", bg="#636e72").place(x=500, y=320)
DataEntry9 = Entry(root3, width=20, textvariable=Sem)
DataEntry9.place(x=500, y=350)

btn1 = Button(root3, text="edite", width=15, height=1, bg="blue", fg="white", command=edite)
btn1.place(x=350, y=500)
btn2 = Button(root3, text="Clear", width=15, height=1, bg="blue", fg="white", command=clears)
btn2.place(x=500, y=500)

root3.mainloop()


