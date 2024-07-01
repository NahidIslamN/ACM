A,B,C,D=input().split()
Average=(float(A)*2 +float(B)*3 +float(C)+ 4 *float(D)*1)/(10)

if Average>=7.0:
    print("Aluno aprovado.")
elif Average<5.0:
    print("Aluno reprovado")
else:
        if 5.0 <=Average:
                if Average>=6.9:
                        print("Aluno em exame.")
                        N=float(input())
                        print("Nota do exame:",N)
                        Sum=(Average+N)/2
                        if Sum>=5.00:
                                print("Aluno reprovado.")
                                print("Media final: {:.1f}".format(Sum))
                
                
                
                
                        
                        
                
                
                
                        
                         
        
        
   
    
    
    
        
