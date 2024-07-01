def bynary_serch(L,x):
    n=len(L)-1
    mid_ind=n//2
    while True:
        if mid_ind==len(L) or mid_ind<-1:
            print(f"x is not found in the List")
            break
        elif L[mid_ind]==x:
            print(f"{x} is found at {mid_ind}")
            break
        if L[mid_ind]>x:
            mid_ind=mid_ind-1
        else:
            mid_ind=mid_ind+1
List=[10,15,20,25,30,35,40,45,50,55,60]
x=60
bynary_serch(List,x)
        
