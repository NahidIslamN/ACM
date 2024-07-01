from csv import reader,writer,DictReader, DictWriter
from tkinter import *
class DelData:
    def __init__(self,m,n):
        self.m=m
        self.n=n
    def Delete_Data(self):

        if self.m=="1st":
            with open('Data files\Computer\C1.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C1.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)

        elif self.m=="2nd":
            with open('Data files\Computer\C2.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C2.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)

        elif self.m=="3rd":
            with open('Data files\Computer\C3.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C3.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)
        elif self.m=="4th":
            with open('Data files\Computer\C4.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C4.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)

        elif self.m=="5th":
            with open('Data files\Computer\C5.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C5.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)
        elif self.m=="6th":
            with open('Data files\Computer\C6.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C6.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)

        elif self.m=="7th":
            with open('Data files\Computer\C7.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C7.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)

        elif self.m=="8th":
            with open('Data files\Computer\C8.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C8.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.n:
                        continue
                    Writer.writerow(row)

def delete():
    m=Entry1.get()
    n=Entry2.get()
    obj=DelData(m,n)
    obj.Delete_Data()
root3 = Tk()
root3.title("Data Entry Form")
root3.configure(background="#636e72")
root3.geometry("650x600")
root3.resizable(0, 0)

text1 = Label(root3, text="Delete Data", fg="white", bg="red")
text1.pack(pady=10, fill="both")
text1.config(font=("impact", 30))

text2 = Label(root3, text="Semester", fg="white", bg="#636e72")
text2.pack(pady=10)
text2.config(font=("impact", 20))

Entry1 = Entry(root3,width=40)
Entry1.pack(pady=(10, 10))


text2 = Label(root3, text="Student ID", fg="white", bg="#636e72")
text2.pack(pady=10)
text2.config(font=("impact", 20))

Entry2 = Entry(root3,width=40)
Entry2.pack(pady=10)

btn1 = Button(root3, text="Delete", width=15, height=1, bg="blue", fg="white", command=delete)
btn1.pack(pady=(25, 10))

root3.mainloop()
