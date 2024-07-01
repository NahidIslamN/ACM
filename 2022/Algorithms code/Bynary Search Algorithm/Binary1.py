# bynary Serch algorithm
def Bynary_serch(L,x):
    N=len(L)
    mid_ind=(N-1)//2
    h1=mid_ind+1
    h2=mid_ind-1
    while True:
        if L[mid_ind]==x:
            print(f"{x} is found at {mid_ind}")
            break
        elif h1>N-1:
            print(f"{x} is not found in the list")
            break
        elif L[h1]==x:
            print(f"{x} is found at {h1}")
            break
        elif h2<0:
            pass
        elif L[h2]==x:
            print(f"{x} is found at {h2}")
            break
        h1=h1+1
        h2=h2-1
List=[1,8,9,6,3,2,5,4,7,25,65,85]
n=85
Bynary_serch(List,n)
