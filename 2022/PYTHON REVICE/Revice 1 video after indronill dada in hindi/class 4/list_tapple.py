'''# Creting a list and accessint the item through the indexing

List=["Nahid Islam","Mahid Islam","Mahim Islam","Monirul Islam","Raihan Tanjim"]
print(List[4])
IN=0
for i in List:
    if i.find("Raihan Tanjim") !=-1:
        M=IN
        break
    IN+=1
print(M)

# Change the list of by using index []
A=[10, 20, 30, 50, 20]
print("before change A is : ",A)
A[2]=60
print("after change A Is : ",A)
# We can create a list in python with defferent type of data
My_List=[600795,"Nahid Islam","Jakaria Islam","Mst. Lovely Begum", 2000, "tk"]

# List methods which i need more very very important
List=[10,20,12,145,52,35,262,5,95,85,675,1,41,52,35,65,85,4,7,41,454,52,4,]
List2=[10,512,620,52,65,85,75,95]
List.extend(List2)
print(List.count(4))
#sorted a list in assinding orderd
List.sort()
print("Assinding Orderd",List)
#sorted a list in desinding orderd
List.sort(reverse=True)
print("Dessinding orderd",List)

#Understand the reverce methond because becase i am learning it frist time
print(List)
List.reverse()
print(List)
List.sort(reverse=True)
print(List)
List.sort()
print(List)

# Appending a item to a list

List.append("Nahid Islam")
for i in List:
    print(i)
List.insert(5,"Mahid Islam")
print(List)

# Create a List of odd Number withe append function
a=int(input())
List=[]
for i in range(2,a+1,2):
    List.append(i)
print(List)

# Deletent item from a list by pop and remove methods
List.pop()
print(List)
List.remove(675)
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].'''



