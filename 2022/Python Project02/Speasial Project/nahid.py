from tkinter import *
from PIL import ImageTk,Image
import os
def images():
    global counter
    img_label.config(image=img_ary[counter % len(img_ary)])
    counter=counter+1   
counter=1
root=Tk()
root.title("baby and baby")
root.minsize(600,500)
root.configure(background="black")

text_label=Label(root,text="Baby ar Baby",fg="pink",bg="black")
text_label.pack(pady=25)
text_label.config(font=("impact",30))

files=os.listdir("baby")
img_ary=[]
for file in files:
    img=Image.open(os.path.join("baby",file))
    resized_img=img.resize((300,300))
    img_ary.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root,image=img_ary[0])
img_label.pack(pady=(10,10))

btn1=Button(root,text="NEXT",fg="white",bg="blue",width=20,height=2,command=images)
btn1.pack(pady=(10,10))
                
root.mainloop()
