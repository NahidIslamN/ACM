N1,N2,N3,N4=map(float,input().split())
Average=(N1*2+N2*3+N3*4+N4*1)/10
print("Media: {:.1f}".format(Average))
if Average>=7.0:
        print("Aluno aprovado.")
elif Average<5.0:
        print("Aluno reprovado.")
elif 5.0 <=Average<=6.9:
        A=float(input())
        print("Aluno em exame.")
        print("Nota do exame:",A)
        Sum=(Average+A)/2
        if Sum>=5.0:
                print("Aluno aprovado.")
                print("Media final: {:.1f}".format(Sum))
        else:
                print("Aluno reprovado.")
                print("Media final: {:.1f}".format(Sum))
