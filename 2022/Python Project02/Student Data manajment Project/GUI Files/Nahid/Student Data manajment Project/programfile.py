from csv import writer,reader,DictReader,DictWriter
from tkinter import *
from PIL import ImageTk,Image


def run_program():
    a=email_entry.get()
    b=password_entry.get()
    c="n"
    d="1"
    if a==c and b==d:
        import Fanction
    else:
        pass
root=Tk()
root.title("Student Data Management System")
root.iconbitmap("icon.ico")
root.maxsize(500,650)
root.minsize(500,650)
root.configure(background="#636e72")

img=Image.open("head.png")
resized=img.resize((500,60))
img=ImageTk.PhotoImage(resized)
img_label=Label(root,image=img)
img_label.pack(pady=(4,4))

text_label=Label(root,text="Student Data Management System",fg="white",bg="#636e72")
text_label.pack(pady=(10,10))
text_label.config(font=("impact",18))

email_label=Label(root,text="Enter Your Email", fg="white",bg="#636e72")
email_label.pack(pady=(110,10))
email_label.config(font=("arial black",15))

email_entry=Entry(root,width=40)
email_entry.pack(ipady=3)

passowrd_label=Label(root,text="Enter Your Password",fg="white",bg="#636e72")
passowrd_label.pack(pady=(30,10),ipady=4)
passowrd_label.config(font=("arial black",15))

password_entry=Entry(root,width=40)
password_entry.pack(ipady=4)

Buttnn=Button(root,text="login",bg="blue",width=20,command= run_program)
Buttnn.pack(pady=(20,10))
















'''while True:
    choice=input("Enter the choice : ")
    if choice=='add data':
        a=input("Enter the Student ID (Carefully) : ")
        b=input("Enter the Student Name : ")
        c=input("Enter the Department : ")
        d=input("Enter the Session : ")
        e=input("Enter the Semester : ")
        f=input("Enter the Shift : ")
        g=input("Enter the Group : ") 
        Contolar=Students()
        Contolar.Add_New_Data(a,b,c,d,e,f,g)
    elif choice=='show details':
        choice2=int(input("Enter 0 for departmental stutas and 1 for all details : "))
        if choice2==1:
            Dep_Stu=AccessStudentData()
            x=input("Enter the student Id : ")
            y=input("semester : ")            
            Dep_Stu.Show_All_Details(x,y)
        elif choice2==0:
            Dep_Stu=AccessStudentData()
            x=input("Enter the student Id : ")
            y=input("semester : ")             
            Dep_Stu.Show_Departmental_Status(x,y)
    elif choice=='edite data':
            DD=DelData()
            x=input("Enter 0(Departmental),1(personal) : ")
            y=input("Enter Semester : ")
            z=input("Enter the SID to Adite or Delete Data Data : ")
            DD.Adite_Data(x,y,z)
    elif choice=='delete data':
            DD=DelData()
            x=input("Enter Semester : ")
            y=input("Enter Student ID : ")
            DD.Delete_Data(x,y)
    elif choice=='add marks':
        while True:
            choice=int(input("Enter 1 for add again 0 for quite : "))
            if choice==1:
                Mark_inp=Mark_input()
                x=input("Enter Semester : ")
                y=input("Enter Student ID : ")
                Mark_inp.add_marks(x,y)
            elif choice==0:
                break
            else:
                print("Enter 0 or 1 to give me right instraction")
    elif choice=='get result':
            X=Result()
            x=input("Enter the Student roll to get result : ")
            y=input("Enter the Student Semester : ")
            X.Result_With_Details(x,y)
    elif choice=='exit':
        break
    else:
        pass '''
    

