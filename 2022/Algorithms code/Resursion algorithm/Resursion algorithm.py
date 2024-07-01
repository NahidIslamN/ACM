# Recursion algorithm and python implyment
def Resursion(n):
    if n==1:
        return 1
    return n+Resursion(n-1)
print(Resursion(10))
