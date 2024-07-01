import math
A,B,C=input().split()
A2=float(A)
B2=float(B)
C2=float(C)
D=pow(B2,2)-(4*A2*C2)
if D>0:
    X1=(-B2+math.sqrt(D))/(2*A2)
    print("R1 = {:.5f}".format(X1))
    X2=(-B2-math.sqrt(D))/(2*A2)
    print("R1 = {:.5f}".format(X2))

