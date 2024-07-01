from tkinter import*
from csv import writer,reader,DictReader,DictWriter

class Students:
    Collage="Thakurgaon Polytechnic Institute"
    def Add_New_Data(self,Student_ID, Student_Name,Department,Session,Semester,Shift,Group):
        self.Student_ID=Student_ID
        self.Student_Name=Student_Name
        self.Department=Department
        self.Session=Session
        self.Semester=Semester
        self.shift=Shift
        self.Group=Group
        
        Head =("Student ID","Student Name","Department","Session","Semester","Shift","Group")
# thes program will detected the student condition and save data acroding to his semester
        Data=(self.Student_ID,self.Student_Name,self.Department,self.Session,self.Semester,self.shift,self.Group)
        if (self.Semester=="1st"):
            with open('Data files\\Computer\\C1.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (self.Semester=="2nd"):
            with open('Data files\\Computer\\C2.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (self.Semester=="3rd"):
            with open('Data files\\Computer\\C3.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (self.Semester=="4th"):
            with open('Data files\\Computer\\C4.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (self.Semester=="5th"):
            with open('Data files\\Computer\\C5.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (self.Semester=="6th"):
            with open('Data files\\Computer\\C6.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (self.Semester=="7th"):
            with open('Data files\\Computer\\C7.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (self.Semester=="8th"):
            with open('Data files\\Computer\\C8.csv', 'a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)

def adder():
    a=Student_ID.get()
    b=Student_Name .get()
    c=Department.get()
    d=Session.get()
    e=Semester.get()
    f=Shift.get()
    g=Group.get()
    x=Students()
    x.Add_New_Data(a,b,c,d,e,f,g)
def clears():
    DataEntry1.delete(0,END)
    DataEntry2.delete(0,END)
    DataEntry3.delete(0,END)
    DataEntry4.delete(0,END)
    DataEntry5.delete(0,END)
    DataEntry6.delete(0,END)
    DataEntry7.delete(0,END)


root3 = Tk()
root3.title("Data Entry Form")
root3.configure(background="#636e72")
root3.geometry("650x600")
root3.resizable(0, 0)

text1 = Label(root3, text="Registration Form", fg="white", bg="red")
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
Semester = StringVar()
Shift = StringVar()
Group = StringVar()

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

btn1=Button(root3,text="Add",width=15,height=1,bg="blue",fg="white",command=adder).place(x=350,y=500)
btn2=Button(root3,text="clear",width=15,height=1,bg="blue",fg="white",command=clears).place(x=500,y=500)

root3.mainloop()
