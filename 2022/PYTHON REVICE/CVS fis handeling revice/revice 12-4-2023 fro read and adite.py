from csv import writer,reader,DictWriter,DictReader

with open ('nn.csv','r') as file:
    head=("Name","Roll","Department")
    Dreader=DictReader(file,fieldnames=head,lineterminator='\n')
    for row in Dreader:
        print(row)

 



    

        


        

        


    
