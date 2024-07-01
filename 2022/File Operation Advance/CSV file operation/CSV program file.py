#edite data with csv file
from csv import writer,reader,DictWriter,DictReader
with open (r'N.csv','r') as file:
    head=("Name","Roll","Dep")
    Reader=DictReader(file,fieldnames=head)
    DR=list(Reader)
with open(r'N.csv','w') as file:
    Writer=DictWriter(file,fieldnames=head,lineterminator='\n')
    for x in DR:
        if x["Roll"] =="600797":
            x["Name"]="Md. Mahid Islam"
            x["Roll"]="600501"
            x["Dep"]="CSE"
        Writer.writerow(x)
        

'''
    head=("Name","Roll","Dep")
    Writer=DictWriter(file,fieldnames=head,lineterminator='\n')
    data=(
        {
            "Name":"Nahid Islam",
            "Roll":"600795",
            "Dep":"CST"
            },
        {
            "Name":"Mahid Islam",
            "Roll":"600797",
            "Dep":"CST"
            },
        {
            "Name":"Nifad Islam",
            "Roll":"600801",
            "Dep":"CST"
            }
        )
    Writer.writeheader()
    Writer.writerows(data)'''
    
