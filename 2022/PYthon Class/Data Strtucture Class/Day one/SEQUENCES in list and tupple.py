#SEQUENCESS in python

List=[10,30,20,10,10,20,20,30,50,40,50,60,40,50,60,70,80,90]
Tup=(10,30,20,10,10,20,20,30,50,40,50,60,40,50,60,70,80,90)
Str='my mother name is mst lovely begum'
List2=[10,30,20,10,10,20,20,30,50,40,50,60,40,50,60,70,80,90]
Tup2=(10,30,20,10,10,20,20,30,50,40,50,60,40,50,60,70,80,90)
Str2='my mother name is mst lovely begum'

# 01 Length
print(len(List))
print(len(Tup))
print(len(Str))

# 02 Select Item
print(List[10])
print(Tup[10])
print(Str[10])

# 03 Slice @ For accessing a prat of a str, list,tupple etc is claed slice
print(List[10:21])
print(Tup[10:21])
print(Str[10:21])

# 04 Count: to count a specific crecter of element from a list,str, tup
print(List.count(20))
print(Tup.count(10))
print(Str.count("m"))

# 05 Index: to find the index of a chr or element of a list, tup or str:
print(List.index(20))
print(Tup.index(10))
print(Str.index("m"))

# 06 Member Shif: to check a specific item is present or not in the variable
print('m' in Str)
print(10 not in Tup)
print(10 in Tup)
print(20 in List)

# 07 Concaneted : Join a tow or more list with concaneted operator "+"
print(List+List2)
print(Tup+Tup2)
print(Str+" "+Str2)

# 08 Mininum: Find out the minimum value from a List or tupple: but the element should be int number of thes tup or list
print(min(List))

# 08 Maxnum: Find out the maxmum value from a List or tupple: but the element should be int number of thes tup or list
print(max(Tup))

# Sum : Get the sum of any list or tuple: but the element should be int
print(sum(List))












