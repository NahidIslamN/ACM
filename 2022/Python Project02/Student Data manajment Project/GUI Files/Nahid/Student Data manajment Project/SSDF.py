from csv import DictReader
from tkinter import *
from PIL import ImageTk, Image

class AccessStudentData:
    def __init__(self):
        self.m = None
        self.n = None
        self.o = None
        self.p = None
        self.q = None
        self.r = None
        self.s = None

    def Show_Departmental_Status(self, a, b):
        self.a = a
        self.b = b
        if self.b == "1st":
            with open('Data files/Computer/C1.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]

        elif self.b == "2nd":
            with open('Data files/Computer/C2.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]
        elif self.b == "3rd":
            with open('Data files/Computer/C3.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]
        elif self.b == "4th":
            with open('Data files/Computer/C4.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]
        elif self.b == "5th":
            with open('Data files/Computer/C5.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]
        elif self.b == "6th":
            with open('Data files/Computer/C6.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]
        elif self.b == "7th":
            with open('Data files/Computer/C7.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]
        elif self.b == "8th":
            with open('Data files/Computer/C8.csv', 'r') as file:
                header = ("Student ID", "Student Name", "Department", "Session", "Semester", "Shift", "Group")
                Reader = DictReader(file, fieldnames=header)
                for row in Reader:
                    if row["Student ID"] == self.a:
                        self.m = row["Student ID"]
                        self.n = row["Student Name"]
                        self.o = row["Department"]
                        self.p = row["Session"]
                        self.q = row["Semester"]
                        self.r = row["Shift"]
                        self.s = row["Group"]

def show():
    global x
    x = AccessStudentData()
    x.Show_Departmental_Status(DataEntry8.get(), DataEntry9.get())
    Student_ID.set(x.m)
    Student_Name.set(x.n)
    Department.set(x.o)
    Session.set(x.p)
    Semester.set(x.q)
    Shift.set(x.r)
    Group.set(x.s)

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

btn1 = Button(root3, text="Show", width=15, height=1, bg="blue", fg="white", command=show)
btn1.place(x=350, y=500)
btn2 = Button(root3, text="Clear", width=15, height=1, bg="blue", fg="white", command=clears)
btn2.place(x=500, y=500)

root3.mainloop()





