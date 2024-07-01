# Linear Search in data structure and algorithm
def LS (L,x):
    i=0
    for j in L:
        if j==x:
            print(f"{x} is found at {i}")
            break
        elif i==len(L)-1:
            print("x is not found in the List")
        i=i+1 

List=[20,30,50,60,10,70,80,50,50,12,45,5]
n=2
LS(List,n)



