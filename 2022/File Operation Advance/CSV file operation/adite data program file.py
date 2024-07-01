from csv import DictWriter
with open("Student.csv","w") as file:
    head=("Name","Department","Roll")
    Writer=DictWriter(file,fieldnames=head,lineterminator='\n')
    data={
        {"Name":"Nahid Islam",
         "Department":"CST",
         "Roll":"600795"},
        }
    Writer.writeheader()
    for x in data:
        Writer.Writerow(x)
