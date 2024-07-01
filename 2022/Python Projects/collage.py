# তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করা পদ্ধতি শুরু
X = int(input("Enter your First Value of X :"))
Y = int(input("Enter your second value of Y: "))
Z = int(input("Enter yoru third value of Z : "))
if X>Y:
    if X>Z:
        print("X is the largest value :",X)
    else:
        print("Largest value is Z : ",Z)
else:
    if Y>Z:
        print("The largest value is Y",Y)
    else:
        print("largest valu is Z",Z)

# তিনটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করা পদ্ধতি শেষ।





# চারটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করার পদ্ধতি শুরু 
#X = int(input("Enter your First Value of X :"))
#Y = int(input("Enter your second value of Y: "))
#Z = int(input("Enter yoru third value of Z : "))
#A = int(input("Enter your 4th value of A : "))

#if (X>Y):
#    if(X>Z):
#        if(X>A):
#            print("Largest value is X =  ",X)
#        else:
#            print("largest value is A = ",A)
#    else:
#        if Z>A:
#            print("largest value is Z = ",Z)
#        else:
#           print("largest value is A = ",A)
#else:
#    if (Y>Z):
#        if (Y>A):
#            print("Largest value is Y = ",Y)
#        else:
#            print("Largest value is A = ",A)
#    else:
#        if (Z>A):
#            print("Largest value is Z = ",Z)
#        else:
#            print("Largest value is A = ",A)

# চারটি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করার পদ্ধতি শেষ।



# 5 টি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করার পদ্ধতি শুরু।

            



# # 5 টি সংখ্যার মধ্যে সবচেয়ে বড় সংখ্যা বের করার পদ্ধতি শুরু।
#X = int(input("Enter your First Value of X :"))
#Y = int(input("Enter your second value of Y: "))
#Z = int(input("Enter yoru third value of Z : "))
#A = int(input("Enter your 4th value of A : "))
#B = int(input("Enter your 5th Value of B :"))
#if (X>Y):
#    if(X>Z):
#        if(X>A):
#            if(X>B):
#                print("The largest value is X : ", X)
#            else:
#                print("The largest Value is B : ", B)
#        else:
#            if(A>B):
#                print("The largest Value is A : ", A)
#            else:
#                print("The largest value is B : ", B)
#    else:
#        if(Z>A):
#            if(Z>B):
#                print("The largest value is Z : ", Z)
#            else:
#                print("The largest value is B : ", B)
#       else:
#            if(A>B):
#                print("The largest value is A : ", A)
#            else:
#                print("The largest value is B : ", B)
#else:
#    if(Y>Z):
#        if(Y>A):
#            if(Y>B):
#                print("The largest value is Y : ", Y)
#            else:
#                print("The largest value is B : ", B)
#        else:
#            if(A>B):
#                print("The largest value is A : ", A)
#            else:
#                print("The largest value is B : ", B)
#    else:
#        if(Z>A):
#            if(Z>B):
#                print("The largest Value is Z : ", Z)
#            else:
#                print("The largest value is B : ", B)
#        else:
#            if(A>B):
#                print("The largest Value is A : ", A)
#            else:
#                print("The largest value is B : ", B)
                
# 5 5 টি সংখ্যার মদ্যে সবচেয়ে বড় সংখ্যা বের করার পদ্ধতি শেষ।
import math
A = int(input("Enter The First Base: "))
B = int(input("Enter The Second Base: "))
C = int(input("Enter The Third Base: "))

if (A+B)> C and (B+C)>A and (C+A)>B :
    S = (A+B+C)/2
    Area = math.sqrt(S*(S-A)*(S-B)*(S-C))
    print((Area))
else:
    print("Traiangle Is Not possible")
