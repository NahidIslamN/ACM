List1=[10,20,30,202,10,10]

# assign a list in a variable
List2=List1
print(List2)
List1[0]="Nahid Islam"
print(List1)
print(List2)

# copy a list
List3=list(List2)
print(List3)
List1[0]=20
print(List1)
print(List3)

# an Impotant Statement List Stracture
#Syntax
#Variable=[operation (n*5) for n in AnyList(list element should be integer value)]
List22=[x*5 for x in List1]
print(List22)

