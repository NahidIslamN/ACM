# Buble short Algorithm Serch algorithm
def Buble_Sort(L):
    for x in range(len(L)-1,0,-1):
        for j in range(x):
            if L[j]>L[j+1]:
                h=L[j]
                L[j]=L[j+1]
                L[j+1]=h
    
List=[45,85,95,25,65,45,15,25,10,35,8556,54,52]
Buble_Sort(List)
print(List)
