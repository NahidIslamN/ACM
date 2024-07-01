# Buble Short in data structure and algorithm
def BS (L):
    for i in range(len(L)-1,0,-1):
        for j in range(i):
            if L[j]>L[j+1]:
                h=L[j]
                L[j]=L[j+1]
                L[j+1]=h
List=[20,30,50,60,70,80,50,50,12,45,5]
BS(List)
print(List)


