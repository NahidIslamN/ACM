'''from csv import writer,DictWriter
with open('nnn.csv','a') as file:
    head=("Name","Roll","Department")
    Writer=DictWriter(file,fieldnames=head,lineterminator='\n')
    Data=(
        {
            "Name":"Tarek Monowar",
            "Roll":"600601",
            "Department":"Food"
            },
        {
            "Name":"Tarikul Islam",
            "Roll":"600602",
            "Department":"Food"
            },
        {
            "Name":"Tripti Rani",
            "Roll":"600603",
            "Department":"Food"
            },
        {
            "Name":"Tisha Islam",
            "Roll":"600604",
            "Department":"Food"
            },
        {
            "Name":"Bonny Akter",
            "Roll":"600605",
            "Department":"Food"
            }
        )
    
    Writer.writerows(Data)
'''
with open (r'result_2nd.pdf','a+') as result:
    x=result.read()
    x.replace("600765 (2.60)","600765 (3.60)")






    
