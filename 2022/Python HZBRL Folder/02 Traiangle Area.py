import math
A = int(input("Enter The First Base: "))
B = int(input("Enter The Second Base: "))
C = int(input("Enter The Third Base: "))

if (A+B)> C and (B+C)>A and (C+A)>B :
    S = (A+B+C)/2
    Area = math.sqrt(S*(S-A)* (S-B) *(S-C))
    print("KhetroFal = ",Area)
    print("Porishima = ",A+B+C)
else:
    print("Traiangle Is Not Possible")
