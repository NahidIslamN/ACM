# creae a dictionary........
'''syntax:

Dictionary_Name={
    "key" : "value",
    "key2","value2",
    "key3","value3"
    }'''

My_Dict={
    "Name" : "Nahid Islam",
    "Father" :"Md Zakaria Islam",
    "Mother" : "Mst. Lovely Begum",
    "Selary":"25000 tk"
    }

update_dict={
    "Name":"Mahid Islam",
    "Nahid":"A programmer",

    }


#My_Dict.update(update_dict)
#print(My_Dict)

# Creating a set in python

my_set={10,20,10,20,30,20,10,20,540,52,62}
#print(type(my_set))
my_set.add(600)
#print(my_set)
my_set.remove(30)
print(my_set)

b=set()
List=[10,50,60,20,10,12,20,10,10,2,0,360,10,40,20,50,30,20,70,10,20,40]
for i in List:
    b.add(i)

print(b)

my_set.intersection(b)
print(my_set)

















