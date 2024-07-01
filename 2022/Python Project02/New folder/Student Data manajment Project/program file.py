from csv import writer,reader,DictReader,DictWriter
#Warning on the avobe are the import state maent Don't make any change!

#  @@@@@@@@@@@ ADDING DATA SECTION @@@@@@@@@@

class Students:
    Collage="Thakurgaon Polytechnic Institute"
    def Add_New_Data(self):
        #Input Student Departmental Status  and store them in a csv fiel in a specific directory
        Student_ID=input("Enter the Student ID (Carefully) : ")
        Student_Name=input("Enter the Student Name : ")
        Department=input("Enter the Department : ")
        Session=input("Enter the Session : ")
        Semester=input("Enter the Semester : ")
        Shift=input("Enter the Shift : ")
        Group=input("Enter the Group : ")
        Head =("Student ID","Student Name","Department","Session","Semester","Shift","Group")

# thes program will detected the student condition and save data acroding to his semester

        Data=(Student_ID,Student_Name,Department,Session,Semester,Shift,Group)
        if (Semester=="1st"):
            with open ('Data files\Computer\C1.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (Semester=="2nd"):
            with open ('Data files\Computer\C2.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (Semester=="3rd"):
            with open ('Data files\Computer\C3.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (Semester=="4th"):
            with open ('Data files\Computer\C4.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (Semester=="5th"):
            with open ('Data files\Computer\C5.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (Semester=="6th"):
            with open ('Data files\Computer\C6.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (Semester=="7th"):
            with open ('Data files\Computer\C7.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)
        elif (Semester=="8th"):
            with open ('Data files\Computer\C8.csv','a') as file:
                 Writer=writer(file,lineterminator='\n')
                 Writer.writerow(Data)

#Input Personal Informathion of a student by theis function and save data into a csv file in a specific directory

        def Personla_Data(a,b):
            SID=Student_ID
            Contact=input("Enter Contact : " )
            Gmail=input("Enter Gmail : " )
            Student_Type=input("Enter Student_Type : " )
            Father=input("Enter Father Name : " )
            Mother=input("Enter Mother : " )
            Divission=input("Enter Divission : " )
            Dictict=input("Enter Dictict : " )
            Upozilla=input("Enter Upozilla : " )
            Village=input("Enter Village : " )        
            if (b=="1st"):
                with open ('Data files\Parsonal Details\C1.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)
            elif (b=="2nd"):
                with open ('Data files\Parsonal Details\C2.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)
            elif (b=="3rd"):
                with open ('Data files\Parsonal Details\C3.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)
            elif (b=="4th"):
                with open ('Data files\Parsonal Details\C4.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)
            elif (b=="5th"):
                with open ('Data files\Parsonal Details\C5.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)           
            elif (b=="6th"):
                with open ('Data files\Parsonal Details\C6.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)
            elif (b=="7th"):
                with open ('Data files\Parsonal Details\C7.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)
            elif (b=="8th"):
                with open ('Data files\Parsonal Details\C8.csv','a') as file:
                    header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                    Writer=DictWriter(file,fieldnames=header,lineterminator='\n')
                    Data={
                        "SID":Student_ID,
                        "Contact":Contact,
                        "Gmail":Gmail,
                        "Student_Type":Student_Type,
                        "Father":Father,
                        "Mother":Mother ,
                        "Divission" :Divission ,
                        "Dictict":Dictict ,
                        "Upozilla":Upozilla,
                        "Village":Village
                        }
                    Writer.writerow(Data)
        Personla_Data(Department,Semester) #This Department and Semester is user input wich was input at frist
#  @@@@@@@@@@@ THE END ADDING DATA SECTION @@@@@@@@@@

#  @@@@@@@@@@@ THE SECTION OF ACCESSING DATA @@@@@@@@@@
class AccessStudentData:
    def Show_Departmental_Status(self,a,b):
        self.a=a
        self.b=b
        if self.b=="1st":
            with open('Data files\Computer\C1.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="2nd":
            with open('Data files\Computer\C2.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="3rd":
            with open('Data files\Computer\C3.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="4th":
            with open('Data files\Computer\C4.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="5th":
            with open('Data files\Computer\C5.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="6th":
            with open('Data files\Computer\C6.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="7th":
            with open('Data files\Computer\C7.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="8th":
            with open('Data files\Computer\C8.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])            
###-----------------------accessing the departmental part is complete------------------------------------------------

#-------------------accessing all the detail of the sutdent(gpa will be incluted into in this function letter)--------------
    def Show_All_Details(self,a,b):
        self.a=a
        self.b=b
        if self.b=="1st":
            with open('Data files\Computer\C1.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C1.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="2st":
            with open('Data files\Computer\C2.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C2.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="2nd":
            with open('Data files\Computer\C2.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C2.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="3rd":
            with open('Data files\Computer\C3.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C3.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="4th":
            with open('Data files\Computer\C4.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C4.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="5th":
            with open('Data files\Computer\C5.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C5.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="6th":
            with open('Data files\Computer\C6.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C6.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="7th":
            with open('Data files\Computer\C7.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C7.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
        elif self.b=="8th":
            with open('Data files\Computer\C8.csv','r') as file:
                header=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["Student ID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
            with open('Data files\Parsonal Details\C8.csv','r') as file:
                header=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                Reader=DictReader(file,fieldnames=header)
                for row in Reader:
                    if row["SID"]==self.a:
                        for i in row:
                            print(i, ":",row[i])
#  @@@@@@@@@@@ THE SECTION OF ACCESSING DATA SUCCESSFULLY COMPLETED @@@@@@@@@@ note(# a fiture incompltet if student mark inputed marke=gpe and befor implement makrk gpe blank) 

#  @@@@@@@@@@@ THE SECTION OF INPUTING MARKS @@@@@@@@@@
class Mark_input:
    def add_marks(self,Semester,ID):
        self.Semester=Semester
        self.ID=ID
        if self.Semester=="1st":
            a=input("Marks of 21011 : ")
            b=input("Marks of 25711 : ")
            c=input("Marks of 25712 : ")
            d=input("Marks of 25911 : ")
            e=input("Marks of 25912 : ")
            f=input("Marks of 26611 : ")
            g=input("Marks of 26711 : ")
            Data=(self.ID,a,b,c,d,e,f,g)
            with open ('Data files\Marks Status\C1.csv','a') as file:
                Writer=writer(file,lineterminator='\n')
                Writer.writerow(Data)
        if self.Semester=="2nd":
            a=input("Marks of 25721 : ")
            b=input("Marks of 25722 : ")
            c=input("Marks of 25812 : ")
            d=input("Marks of 25921 : ")
            e=input("Marks of 25922 : ")
            f=input("Marks of 26621 : ")
            g=input("Marks of 26622 : ")
            h=input("Marks of 26811 :")
            Data=(self.ID,a,b,c,d,e,f,g,h)
            with open ('Data files\Marks Status\C2.csv','a') as file:
                Writer=writer(file,lineterminator='\n')
                Writer.writerow(Data)
        if self.Semester=="3rd":
            a=input("Marks of 21811 : ")
            b=input("Marks of 25913 : ")
            c=input("Marks of 25931 : ")
            d=input("Marks of 26631 : ")
            e=input("Marks of 26632 : ")
            f=input("Marks of  26633 : ")
            g=input("Marks of 26831 : ")
            Data=(self.ID,a,b,c,d,e,f,g)
            with open ('Data files\Marks Status\C3.csv','a') as file:
                Writer=writer(file,lineterminator='\n')
                Writer.writerow(Data)
        if self.Semester=="4th":
            a=input("Marks of 25831: ")
            b=input("Marks of 26641 : ")
            c=input("Marks of 26642 : ")
            d=input("Marks of 26643 : ")
            e=input("Marks of 26644 : ")
            f=input("Marks of  26841 : ")
            g=input("Marks of 29041 : ")
            Data=(self.ID,a,b,c,d,e,f,g)
            with open ('Data files\Marks Status\C4.csv','a') as file:
                Writer=writer(file,lineterminator='\n')
                Writer.writerow(Data)
        if self.Semester=="5th":
            a=input("Marks of 25841 : ")
            b=input("Marks of 26651 : ")
            c=input("Marks of 26652 : ")
            d=input("Marks of 26653 : ")
            e=input("Marks of 26654 : ")
            f=input("Marks of  26655 : ")
            g=input("Marks of 26656 : ")
            Data=(self.ID,a,b,c,d,e,f,g)
            with open ('Data files\Marks Status\C5.csv','a') as file:
                Writer=writer(file,lineterminator='\n')
                Writer.writerow(Data)            
        if self.Semester=="6th":
            a=input("Marks of 25851 : ")
            b=input("Marks of 25852 : ")
            c=input("Marks of 26661 : ")
            d=input("Marks of 26662 : ")
            e=input("Marks of 26664 : ")
            f=input("Marks of  26665 : ")
            g=input("Marks of 26666 : ")
            Data=(self.ID,a,b,c,d,e,f,g)
            with open ('Data files\Marks Status\C6.csv','a') as file:
                Writer=writer(file,lineterminator='\n')
                Writer.writerow(Data)
        if self.Semester=="7th":
            a=input("Marks of 25853 : ")
            b=input("Marks of 26671 : ")
            c=input("Marks of 26672 : ")
            d=input("Marks of 26673 : ")
            e=input("Marks of 26675 : ")
            f=input("Marks of  26676 : ")
            Data=(self.ID,a,b,c,d,e,f)
            with open ('Data files\Marks Status\C7.csv','a') as file:
                Writer=writer(file,lineterminator='\n')
                Writer.writerow(Data)             
                  
#  @@@@@@@@@@@ THE SECTION OF INPUTING MARKS SUCCESSFULLY COMPLETED @@@@@@@@@@ 

#  @@@@@@@@@@@ THE SECTION OF DELETE ADITE DATA FROM THE STUDENT LIST @@@@@@@@@@
class DelData:
    def Delete_Data(self,Semester,SID):
        self.Semester=Semester
        self.SID=SID
        if self.Semester=="1st":
            with open('Data files\Computer\C1.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C1.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C1.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C1.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)
        elif self.Semester=="2nd":
            with open('Data files\Computer\C2.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C2.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C2.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C2.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)
        elif self.Semester=="3rd":
            with open('Data files\Computer\C3.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C3.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C3.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C3.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)
        elif self.Semester=="4th":
            with open('Data files\Computer\C4.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C4.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C4.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C4.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)
        elif self.Semester=="5th":
            with open('Data files\Computer\C5.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C5.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C5.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C5.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)
        elif self.Semester=="6th":
            with open('Data files\Computer\C6.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C6.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C6.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C6.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

        elif self.Semester=="7th":
            with open('Data files\Computer\C7.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C7.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C7.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C7.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)
        elif self.Semester=="8th":
            with open('Data files\Computer\C8.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Computer\C8.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

            with open('Data files\Parsonal Details\C8.csv','r') as file:
                Reader=reader(file)
                Data=list(Reader)
            with open('Data files\Parsonal Details\C8.csv','w') as file:
                Writer=writer(file,lineterminator='\n')
                for row in Data:
                    if row[0]==self.SID:
                        continue
                    Writer.writerow(row)

# the section of adite Data of thise program

    def Adite_Data(self,Cetagory,Semester,SID,):#The function of aditing data of departmental Stutas to a sutdent throught his Student Id
        self.Cetagory=Cetagory
        self.Semester=Semester
        self.SID=SID
        if self.Cetagory=="0":
            if self.Semester=="1st":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C1.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C1.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)
            elif self.Semester=="2nd":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C2.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C2.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)
            elif self.Semester=="3rd":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C3.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C3.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)
            elif self.Semester=="4th":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C4.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C4.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)
            elif self.Semester=="5th":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C5.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C5.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)
            elif self.Semester=="6th":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C6.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C6.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)
            elif self.Semester=="7th":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C7.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C7.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)
            elif self.Semester=="8th":
                Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
                with open('Data files\Computer\C8.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Computer\C8.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["Student ID"]==self.SID:
                            row["Student Name"]=input("Enter Student Name : ")
                            row["Department"]=input("Enter Department : ")
                            row["Session"]=input("Enter Session : ")
                            row["Semester"]=input("Enter Semester : ")
                            row["Shift"]=input("Enter Shift : ")
                            row["Group"]=input("Enter Group : ")
                        Writer.writerow(row)                        
                        
        elif self.Cetagory=="1":
            if self.Semester=="1st":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C1.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C1.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)
            if self.Semester=="2nd":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C2.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C2.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)
            if self.Semester=="3rd":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C3.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C3.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)
            if self.Semester=="4th":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C4.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C4.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)
            if self.Semester=="5th":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C5.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C5.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)
            if self.Semester=="6th":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C6.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C6.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)
            if self.Semester=="7th":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C7.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C7.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)
            if self.Semester=="8th":
                Head=("SID","Contact","Gmail","Student_Type","Father","Mother","Divission","Dictict","Upozilla","Village")
                with open('Data files\Parsonal Details\C8.csv','r') as file:
                    Reader=DictReader(file,fieldnames=Head)
                    Data=Reader=list(Reader)
                with open('Data files\Parsonal Details\C8.csv','w') as file:
                    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
                    for row in Data:
                        if row["SID"]==self.SID:
                            row["Contact"]=input("Enter Contact : ")
                            row["Gmail"]=input("Enter Gamail : ")
                            row["Student_Type"]=input("Enter Student_Type : ")
                            row["Father"]=input("Enter Father Name : ")
                            row["Mother"]=input("Enter Mother Name : ")
                            row["Divission"]=input("Enter Divission : ")
                            row["Dictict"]=input("Enter Distict : ")
                            row["Upozilla"]=input("Enter Upozilla : ")
                            row["Village"]=input("Enter Village : ")
                        Writer.writerow(row)                        
# THE SECTION OF GETTEING ALL KIND OF RESULT OF A STUDENT#

class Result:
    def Result_With_Details(self,SID,Sem):
        self.SID=SID
        self.Sem=Sem    
        if self.Sem=="1st":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            Head2=("Student ID","21011","25711","25712","25911","25912","26611","26711")    
            with open('Data files\Computer\C1.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                for row in Reader:
                    if row["Student ID"]==self.SID:
                        for rows in row:
                            print(rows,":",row[rows])                
            with open ('Data files\Marks Status\C1.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head2)
                for row in Reader:                    
                    if row["Student ID"]==self.SID:
                        Result_List=[]
                        for rows in row:
                            Result_List.append(row[rows])
                        if int(Result_List[1])>=90 and int(Result_List[2])>=90 and int(Result_List[3])>=90 and int(Result_List[4])>=90 and int(Result_List[5])>=90 and int(Result_List[6])>=90 and int(Result_List[7])>=90:
                            print("Grade : A+")
                            print("GPA : 4.00")
                        elif int(Result_List[1])>=80 and int(Result_List[2])>=80 and int(Result_List[3])>=80 and int(Result_List[4])>=80 and int(Result_List[5])>=80 and int(Result_List[6])>=80 and int(Result_List[7])>=80:
                            print("Grade : A")
                            print("GPA : 3.80")
                        elif int(Result_List[1])>=70 and int(Result_List[2])>=70 and int(Result_List[3])>=70 and int(Result_List[4])>=70 and int(Result_List[5])>=70 and int(Result_List[6])>=70 and int(Result_List[7])>=70:
                            print("Grade : A-")
                            print("GPA : 3.50")
                        elif int(Result_List[1])>=60 and int(Result_List[2])>=60 and int(Result_List[3])>=60 and int(Result_List[4])>=60 and int(Result_List[5])>=60 and int(Result_List[6])>=60 and int(Result_List[7])>=60:
                            print("Grade : B")
                            print("GPA : 3.00")
                        elif int(Result_List[1])>=50 and int(Result_List[2])>=50 and int(Result_List[3])>=50 and int(Result_List[4])>=50 and int(Result_List[5])>=50 and int(Result_List[6])>=50 and int(Result_List[7])>=50:
                            print("Grade : C")
                            print("GPA : 2.00")
                        elif int(Result_List[1])>=40 and int(Result_List[2])>=40 and int(Result_List[3])>=40 and int(Result_List[4])>=40 and int(Result_List[5])>=40 and int(Result_List[6])>=40 and int(Result_List[7])>=40:
                            print("Grade : D")
                            print("GPA : 1.00")
                        else:
                            print("Grade : F")
                            print("GPA : 0.00")
        if self.Sem=="2nd":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            Head2=("Student ID","25721","25722","25812","25921","25922","26621","26622","26811")  
            with open('Data files\Computer\C2.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                for row in Reader:
                    if row["Student ID"]==self.SID:
                        for rows in row:
                            print(rows,":",row[rows])                
            with open ('Data files\Marks Status\C2.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head2)
                for row in Reader:                    
                    if row["Student ID"]==self.SID:
                        Result_List=[]
                        for rows in row:
                            Result_List.append(row[rows])
                        if int(Result_List[1])>=90 and int(Result_List[2])>=90 and int(Result_List[3])>=90 and int(Result_List[4])>=90 and int(Result_List[5])>=90 and int(Result_List[6])>=90 and int(Result_List[7])>=90 and int(Result_List[8])>=90:
                            print("Grade : A+")
                            print("GPA : 4.00")
                        elif int(Result_List[1])>=80 and int(Result_List[2])>=80 and int(Result_List[3])>=80 and int(Result_List[4])>=80 and int(Result_List[5])>=80 and int(Result_List[6])>=80 and int(Result_List[7])>=80 and int(Result_List[8])>=80:
                            print("Grade : A")
                            print("GPA : 3.80")
                        elif int(Result_List[1])>=70 and int(Result_List[2])>=70 and int(Result_List[3])>=70 and int(Result_List[4])>=70 and int(Result_List[5])>=70 and int(Result_List[6])>=70 and int(Result_List[7])>=70 and int(Result_List[8])>=70:
                            print("Grade : A-")
                            print("GPA : 3.50")
                        elif int(Result_List[1])>=60 and int(Result_List[2])>=60 and int(Result_List[3])>=60 and int(Result_List[4])>=60 and int(Result_List[5])>=60 and int(Result_List[6])>=60 and int(Result_List[7])>=60 and int(Result_List[8])>=60:
                            print("Grade : B")
                            print("GPA : 3.00")
                        elif int(Result_List[1])>=50 and int(Result_List[2])>=50 and int(Result_List[3])>=50 and int(Result_List[4])>=50 and int(Result_List[5])>=50 and int(Result_List[6])>=50 and int(Result_List[7])>=50 and int(Result_List[8])>=50:
                            print("Grade : C")
                            print("GPA : 2.00")
                        elif int(Result_List[1])>=40 and int(Result_List[2])>=40 and int(Result_List[3])>=40 and int(Result_List[4])>=40 and int(Result_List[5])>=40 and int(Result_List[6])>=40 and int(Result_List[7])>=40 and int(Result_List[8])>=40:
                            print("Grade : D")
                            print("GPA : 1.00")
                        else:
                            print("Grade : F")
                            print("GPA : 0.00")
        if self.Sem=="3rd":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            Head2=("Student ID","21811","25913","25931","26631","26632","26633","26831")  
            with open('Data files\Computer\C3.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                for row in Reader:
                    if row["Student ID"]==self.SID:
                        for rows in row:
                            print(rows,":",row[rows])                
            with open ('Data files\Marks Status\C3.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head2)
                for row in Reader:                    
                    if row["Student ID"]==self.SID:
                        Result_List=[]
                        for rows in row:
                            Result_List.append(row[rows])
                        if int(Result_List[1])>=90 and int(Result_List[2])>=90 and int(Result_List[3])>=90 and int(Result_List[4])>=90 and int(Result_List[5])>=90 and int(Result_List[6])>=90 and int(Result_List[7])>=90 :
                            print("Grade : A+")
                            print("GPA : 4.00")
                        elif int(Result_List[1])>=80 and int(Result_List[2])>=80 and int(Result_List[3])>=80 and int(Result_List[4])>=80 and int(Result_List[5])>=80 and int(Result_List[6])>=80 and int(Result_List[7])>=80:
                            print("Grade : A")
                            print("GPA : 3.80")
                        elif int(Result_List[1])>=70 and int(Result_List[2])>=70 and int(Result_List[3])>=70 and int(Result_List[4])>=70 and int(Result_List[5])>=70 and int(Result_List[6])>=70 and int(Result_List[7])>=70:
                            print("Grade : A-")
                            print("GPA : 3.50")
                        elif int(Result_List[1])>=60 and int(Result_List[2])>=60 and int(Result_List[3])>=60 and int(Result_List[4])>=60 and int(Result_List[5])>=60 and int(Result_List[6])>=60 and int(Result_List[7])>=60 :
                            print("Grade : B")
                            print("GPA : 3.00")
                        elif int(Result_List[1])>=50 and int(Result_List[2])>=50 and int(Result_List[3])>=50 and int(Result_List[4])>=50 and int(Result_List[5])>=50 and int(Result_List[6])>=50 and int(Result_List[7])>=50 :
                            print("Grade : C")
                            print("GPA : 2.00")
                        elif int(Result_List[1])>=40 and int(Result_List[2])>=40 and int(Result_List[3])>=40 and int(Result_List[4])>=40 and int(Result_List[5])>=40 and int(Result_List[6])>=40 and int(Result_List[7])>=40:
                            print("Grade : D")
                            print("GPA : 1.00")
                        else:
                            print("Grade : F")
                            print("GPA : 0.00")
        if self.Sem=="4th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            Head2=("Student ID","25831","26641","26642","26643","26644","26841","29041")
            with open('Data files\Computer\C4.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                for row in Reader:
                    if row["Student ID"]==self.SID:
                        for rows in row:
                            print(rows,":",row[rows])                
            with open ('Data files\Marks Status\C4.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head2)
                for row in Reader:                    
                    if row["Student ID"]==self.SID:
                        Result_List=[]
                        for rows in row:
                            Result_List.append(row[rows])
                        if int(Result_List[1])>=90 and int(Result_List[2])>=90 and int(Result_List[3])>=90 and int(Result_List[4])>=90 and int(Result_List[5])>=90 and int(Result_List[6])>=90 and int(Result_List[7])>=90 :
                            print("Grade : A+")
                            print("GPA : 4.00")
                        elif int(Result_List[1])>=80 and int(Result_List[2])>=80 and int(Result_List[3])>=80 and int(Result_List[4])>=80 and int(Result_List[5])>=80 and int(Result_List[6])>=80 and int(Result_List[7])>=80:
                            print("Grade : A")
                            print("GPA : 3.80")
                        elif int(Result_List[1])>=70 and int(Result_List[2])>=70 and int(Result_List[3])>=70 and int(Result_List[4])>=70 and int(Result_List[5])>=70 and int(Result_List[6])>=70 and int(Result_List[7])>=70:
                            print("Grade : A-")
                            print("GPA : 3.50")
                        elif int(Result_List[1])>=60 and int(Result_List[2])>=60 and int(Result_List[3])>=60 and int(Result_List[4])>=60 and int(Result_List[5])>=60 and int(Result_List[6])>=60 and int(Result_List[7])>=60 :
                            print("Grade : B")
                            print("GPA : 3.00")
                        elif int(Result_List[1])>=50 and int(Result_List[2])>=50 and int(Result_List[3])>=50 and int(Result_List[4])>=50 and int(Result_List[5])>=50 and int(Result_List[6])>=50 and int(Result_List[7])>=50 :
                            print("Grade : C")
                            print("GPA : 2.00")
                        elif int(Result_List[1])>=40 and int(Result_List[2])>=40 and int(Result_List[3])>=40 and int(Result_List[4])>=40 and int(Result_List[5])>=40 and int(Result_List[6])>=40 and int(Result_List[7])>=40:
                            print("Grade : D")
                            print("GPA : 1.00")
                        else:
                            print("Grade : F")
                            print("GPA : 0.00")
        if self.Sem=="5th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            Head2=("Student ID","25841","26651","26652","26653","26654","2655","26656")
            with open('Data files\Computer\C5.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                for row in Reader:
                    if row["Student ID"]==self.SID:
                        for rows in row:
                            print(rows,":",row[rows])                
            with open ('Data files\Marks Status\C5.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head2)
                for row in Reader:                    
                    if row["Student ID"]==self.SID:
                        Result_List=[]
                        for rows in row:
                            Result_List.append(row[rows])
                        if int(Result_List[1])>=90 and int(Result_List[2])>=90 and int(Result_List[3])>=90 and int(Result_List[4])>=90 and int(Result_List[5])>=90 and int(Result_List[6])>=90 and int(Result_List[7])>=90 :
                            print("Grade : A+")
                            print("GPA : 4.00")
                        elif int(Result_List[1])>=80 and int(Result_List[2])>=80 and int(Result_List[3])>=80 and int(Result_List[4])>=80 and int(Result_List[5])>=80 and int(Result_List[6])>=80 and int(Result_List[7])>=80:
                            print("Grade : A")
                            print("GPA : 3.80")
                        elif int(Result_List[1])>=70 and int(Result_List[2])>=70 and int(Result_List[3])>=70 and int(Result_List[4])>=70 and int(Result_List[5])>=70 and int(Result_List[6])>=70 and int(Result_List[7])>=70:
                            print("Grade : A-")
                            print("GPA : 3.50")
                        elif int(Result_List[1])>=60 and int(Result_List[2])>=60 and int(Result_List[3])>=60 and int(Result_List[4])>=60 and int(Result_List[5])>=60 and int(Result_List[6])>=60 and int(Result_List[7])>=60 :
                            print("Grade : B")
                            print("GPA : 3.00")
                        elif int(Result_List[1])>=50 and int(Result_List[2])>=50 and int(Result_List[3])>=50 and int(Result_List[4])>=50 and int(Result_List[5])>=50 and int(Result_List[6])>=50 and int(Result_List[7])>=50 :
                            print("Grade : C")
                            print("GPA : 2.00")
                        elif int(Result_List[1])>=40 and int(Result_List[2])>=40 and int(Result_List[3])>=40 and int(Result_List[4])>=40 and int(Result_List[5])>=40 and int(Result_List[6])>=40 and int(Result_List[7])>=40:
                            print("Grade : D")
                            print("GPA : 1.00")
                        else:
                            print("Grade : F")
                            print("GPA : 0.00")
        if self.Sem=="6th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            Head2=("Student ID","25851","25852","26661","26662","26664","26665","26666")
            with open('Data files\Computer\C6.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                for row in Reader:
                    if row["Student ID"]==self.SID:
                        for rows in row:
                            print(rows,":",row[rows])                
            with open ('Data files\Marks Status\C6.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head2)
                for row in Reader:                    
                    if row["Student ID"]==self.SID:
                        Result_List=[]
                        for rows in row:
                            Result_List.append(row[rows])
                        if int(Result_List[1])>=90 and int(Result_List[2])>=90 and int(Result_List[3])>=90 and int(Result_List[4])>=90 and int(Result_List[5])>=90 and int(Result_List[6])>=90 and int(Result_List[7])>=90 :
                            print("Grade : A+")
                            print("GPA : 4.00")
                        elif int(Result_List[1])>=80 and int(Result_List[2])>=80 and int(Result_List[3])>=80 and int(Result_List[4])>=80 and int(Result_List[5])>=80 and int(Result_List[6])>=80 and int(Result_List[7])>=80:
                            print("Grade : A")
                            print("GPA : 3.80")
                        elif int(Result_List[1])>=70 and int(Result_List[2])>=70 and int(Result_List[3])>=70 and int(Result_List[4])>=70 and int(Result_List[5])>=70 and int(Result_List[6])>=70 and int(Result_List[7])>=70:
                            print("Grade : A-")
                            print("GPA : 3.50")
                        elif int(Result_List[1])>=60 and int(Result_List[2])>=60 and int(Result_List[3])>=60 and int(Result_List[4])>=60 and int(Result_List[5])>=60 and int(Result_List[6])>=60 and int(Result_List[7])>=60 :
                            print("Grade : B")
                            print("GPA : 3.00")
                        elif int(Result_List[1])>=50 and int(Result_List[2])>=50 and int(Result_List[3])>=50 and int(Result_List[4])>=50 and int(Result_List[5])>=50 and int(Result_List[6])>=50 and int(Result_List[7])>=50 :
                            print("Grade : C")
                            print("GPA : 2.00")
                        elif int(Result_List[1])>=40 and int(Result_List[2])>=40 and int(Result_List[3])>=40 and int(Result_List[4])>=40 and int(Result_List[5])>=40 and int(Result_List[6])>=40 and int(Result_List[7])>=40:
                            print("Grade : D")
                            print("GPA : 1.00")
                        else:
                            print("Grade : F")
                            print("GPA : 0.00")
        if self.Sem=="7th":
            Head=("Student ID","Student Name","Department","Session","Semester","Shift","Group")
            Head2=("Student ID","25853","26671","26672","26673","26675","26676")
            with open('Data files\Computer\C7.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head)
                for row in Reader:
                    if row["Student ID"]==self.SID:
                        for rows in row:
                            print(rows,":",row[rows])                
            with open ('Data files\Marks Status\C7.csv','r') as file:
                Reader=DictReader(file,fieldnames=Head2)
                for row in Reader:                    
                    if row["Student ID"]==self.SID:
                        Result_List=[]
                        for rows in row:
                            Result_List.append(row[rows])
                        if int(Result_List[1])>=90 and int(Result_List[2])>=90 and int(Result_List[3])>=90 and int(Result_List[4])>=90 and int(Result_List[5])>=90 and int(Result_List[6])>=90:
                            print("Grade : A+")
                            print("GPA : 4.00")
                        elif int(Result_List[1])>=80 and int(Result_List[2])>=80 and int(Result_List[3])>=80 and int(Result_List[4])>=80 and int(Result_List[5])>=80 and int(Result_List[6])>=80:
                            print("Grade : A")
                            print("GPA : 3.80")
                        elif int(Result_List[1])>=70 and int(Result_List[2])>=70 and int(Result_List[3])>=70 and int(Result_List[4])>=70 and int(Result_List[5])>=70 and int(Result_List[6])>=70:
                            print("Grade : A-")
                            print("GPA : 3.50")
                        elif int(Result_List[1])>=60 and int(Result_List[2])>=60 and int(Result_List[3])>=60 and int(Result_List[4])>=60 and int(Result_List[5])>=60 and int(Result_List[6])>=60:
                            print("Grade : B")
                            print("GPA : 3.00")
                        elif int(Result_List[1])>=50 and int(Result_List[2])>=50 and int(Result_List[3])>=50 and int(Result_List[4])>=50 and int(Result_List[5])>=50 and int(Result_List[6])>=50:
                            print("Grade : C")
                            print("GPA : 2.00")
                        elif int(Result_List[1])>=40 and int(Result_List[2])>=40 and int(Result_List[3])>=40 and int(Result_List[4])>=40 and int(Result_List[5])>=40 and int(Result_List[6])>=40 and int(Result_List[7])>=40:
                            print("Grade : D")
                            print("GPA : 1.00")
                        else:
                            print("Grade : F")
                            print("GPA : 0.00")         
##-----------------------------the object and function calling part-------------------------------
#'add data', 'show details','delete data','edite data','add marks','get result')
while True:
    choice=input("Enter the choice : ")
    if choice=='add data':
        Contolar=Students()
        Contolar.Add_New_Data()
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
        pass 


