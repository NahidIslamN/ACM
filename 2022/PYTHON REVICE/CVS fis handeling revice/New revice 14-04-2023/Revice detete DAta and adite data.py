from csv import DictWriter,DictReader

with open('Student.csv','r') as file:
    
    Reader=DictReader(file)
    Data=list(Reader)
with open('Student.csv','w') as file:
    Head=("Name","Roll","Department","Marks")
    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
    for row in Data:
        if row["Roll"]=="600601":
            continue
        Writer.writeheader
        Writer.writerow(row)
with open('Student.csv','a') as file:
    Head=("Name","Roll","Department","Marks")
    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
    Update_Data={
        "Name":"Suborna Asrafi",
        "Roll":"600601",
        "Department":"CST",
        "Marks":"3.97"
        }
    Writer.writerow(Update_Data)

    
    
    
