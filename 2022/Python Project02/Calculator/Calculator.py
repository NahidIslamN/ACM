def Add (a,b):
    m=(a+b)
    return m
def Minus(a,b):
    if a<0:
        m=a-b
        return m
    elif a>b:
        m=a-b
        return m
    elif b>a:
        m=-b+a
        return m
def Multiplication (a,b):
    m=a*b
    return m
def devided (a,b):
    m=a/b
    return m
X=int(input("Enter the value of friest number : "))
Y=input("What do you Want? : ")
Z=int(input("Enter the value of second number : "))
if (Y=="+"):
    Result=Add(X,Z)
elif (Y=="-") :
    Result=Minus(X,Z)
elif (Y=="*"):
    Result=Multiplication(X,Z)
elif (Y=="/"):
    Result=devided (X,Z)
print(Result)
