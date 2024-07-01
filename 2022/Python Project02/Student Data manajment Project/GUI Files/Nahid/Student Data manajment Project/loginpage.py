from tkinter import *
from PIL import ImageTk,Image
def run_program():
    a=email_entry.get()
    b=password_entry.get()
    c="n"
    d="1"
    if a==c and b==d:
        pass
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
