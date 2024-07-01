# create a csv file with w mode and write data with w and a mode (with list or tupple)
from csv import writer
with open('Student.csv','w') as file:
    Writer=writer(file,lineterminator='\n')
    Head=("Name","Roll","Department","Marks")
    Data=(
        ("Farabi Islam",600601,"CST",4.00),
        ("Monir Islam",600602,"CST",4.00),
        ("Jalal Islam",600603,"CST",4.00),
        ("Jamiya Islam",600604,"CST",4.00),
        ("Nuri Islam",600605,"CST",4.00),
        ("Nouril Islam",600606,"CST",4.00),
        
        )
    Writer.writerow(Head) # for single tuple of single list
    Writer.writerows(Data) #for ani multi tupple or any multi list
    #or
    '''for x in Data:
        Writer.writerow(Data)'''



# Write data in csv file with dictionary with append or write mode
from csv import DictWriter

with open ('Student.csv','a') as file:
    Head=("Name","Roll","Department","Marks")
    Writer=DictWriter(file,fieldnames=Head,lineterminator='\n')
    Data=(
        {
        "Name":"Rifa Chowdhory",
        "Roll":"600702",
        "Department":"CST",
        "Marks":"4.00"
        },
        {
        "Name":"Riva Khan",
        "Roll":"600703",
        "Department":"CST",
        "Marks":"4.00"
        },
        {
        "Name":"Raka Roy",
        "Roll":"600704",
        "Department":"CST",
        "Marks":"4.00"
        },
        {
        "Name":"Rotna Islam",
        "Roll":"600705",
        "Department":"CST",
        "Marks":"4.00"
        },
        {
        "Name":"Nurol Haque",
        "Roll":"600706",
        "Department":"CST",
        "Marks":"4.00"
        },
        )
    #Writer.writerow(Data) for single dictionary#


    # for multiple dictonary
    '''for x in Data:
        Writer.writerow(x)'''
    #or

    Writer.writerows(Data)
        



