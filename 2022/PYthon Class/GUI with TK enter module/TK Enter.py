from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Student Data management System")
root.iconbitmap("Tpi.ico")
root.maxsize(400,600)
root.minsize(400,400)
root.configure(background="#7d5fff")
img=Image.open("head.png")
resized=img.resize((400,25))
img=ImageTk.PhotoImage(resized)
img_l=Label(root,image=img)
img_l.pack()
text_label=Label(root,text="Student Data management System",fg="white",bg="#7d5fff")
text_label.pack(pady=10)
text_label.config(font=("impact","16"))
emial_label=Label(root,text="Enter your ID",fg="white",bg="#7d5fff")
emial_label.pack(pady=(100,10))
emial_label.config(font=("times new roman",15))

email_entry=Entry(root,width=6)
email_entry.pack()


root.mainloop()
