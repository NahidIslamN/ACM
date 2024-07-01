from tkinter import*
from PIL import ImageTk,Image



def add_new():
    import EntryF  
def show():
    import SSDF
def delete():
    import deletedata
def edit():
    import edite
    
   
root2=Tk()
root2.title("Student Data Management System")
root2.iconbitmap('icon.ico')
root2.maxsize(600,650)
root2.minsize(600,650)
root2.configure(background="blue")

text_Label=Label(root2,text="Function Of The Program",fg="white",bg="blue")
text_Label.pack(pady=(30,110))
text_Label.config(font=("Times new roman",24))

Buttn1=Button(root2,text="Add New", width=60,fg="white",bg="#636e72",command=add_new)
Buttn1.pack(pady=(30,15),ipady=4)

Buttn2=Button(root2,text="Show Student's Data", width=60,fg="white",bg="#636e72",command=show)
Buttn2.pack(pady=(15,15),ipady=4)

Buttn3=Button(root2,text="Delete  Student Record", width=60,fg="white",bg="#636e72",command=delete)
Buttn3.pack(pady=(15,15),ipady=4)

Buttn4=Button(root2,text="Edite  Student Record", width=60,fg="white",bg="#636e72",command=edit)
Buttn4.pack(pady=(15,15),ipady=4)



root2.mainloop()
