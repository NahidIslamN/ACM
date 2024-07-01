#Linear search with while loop
def Linear_Search(L,x):
    i=0
    while True:
        if i==len(L):
            print(f"x is not found in the List")
            break
        elif L[i]==x:
            print(f"{x} is found at {i}")
            break
        i=i+1
List=[10,15,20,25,30,35,40,45,50,55,60]
x=5
#Linear_Search(List,x)
# Linear Search with for loop
def Linear_Search2(L,x):
    j=0
    for i in L:
        if j==len(L)+1:
            print(f"{x} is not found in the List")
            break
        elif i==x:
            print(f"{x} is found at {j}")
            break
        j=j+1
List=[10,15,20,25,30,35,40,45,50,55,60,61,53]
x=53
Linear_Search2(List,x)

        
