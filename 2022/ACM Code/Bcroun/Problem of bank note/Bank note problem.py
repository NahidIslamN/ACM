N=int(input())
print(N)
notes=[100,50,20,10,5,2,1]
result1=[]
result2=[]
result3=[]
result4=[]
result5=[]
result6=[]
result7=[]
for note in notes:
    while N>=note:
        if note==100:
            result1.append(note)
        elif note==50:
            result2.append(note)
        elif note==20:
            result3.append(note)
        elif note==10:
            result4.append(note)
        elif note==5:
            result5.append(note)
        elif note==2:
            result6.append(note)
        elif note==1:
            result7.append(note)        
        N=N-note
print(len(result1),"nota(s) de R$ 100,00")
print(len(result2),"nota(s) de R$ 50,00")
print(len(result3),"nota(s) de R$ 20,00")
print(len(result4),"nota(s) de R$ 10,00")
print(len(result5),"nota(s) de R$ 5,00")
print(len(result6),"nota(s) de R$ 2,00")
print(len(result7),"nota(s) de R$ 1,00")



