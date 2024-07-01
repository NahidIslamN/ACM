'''def Hellow(a="Nahid",b="Nahid",c="Nahid"):
    print("Hellow Mr",a)
    print("Hellow Mr",b)
    print("Hellow Mr",c)
Hellow("Mahid","Rimon")'''

# print the factorial number by using function in python
'''def Factorial(n):
    Product=1
    for i in range(1,n+1):
        Product=Product*i
    return Product

    
F=Factorial(5)
print(F)'''

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)
F=factorial_recursive(5)
print(F)


