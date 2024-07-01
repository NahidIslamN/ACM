def margesort(L):
    if len(L)>1:
        mid_ind=len(L)//2
        List1=L[:mid_ind]
        List2=L[mid_ind:]
        margesort(List1)
        margesort(List2)
        i,j,k=0,0,0
        while i<len(List1) and j<len(List2):
            if List1[i]<List2[j]:
                L[k]=List1[i]
                i=i+1
                k=k+1
            else:
                L[k]=List2[j]
                j=j+1
                k=k+1
        while i<len(List1):
            L[k]=List1[i]
            i=i+1
            k=k+1
        while j<len(List2):
            L[k]=List2[j]
            j=j+1
            k=k+1        
'''n=int(input("Enter element numbers : "))
List=[int(input("Enter the elements : " ) for x in range(n)]'''
List=[1,5,2,4,3]
margesort(List)
print(List)
    
