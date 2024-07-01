# While loop in python

'''syntax
while condition:   # if condition ture loop will exicude untill condition false
    looping body if condition ture
    loop initialigation

for example'''
'''L=[]
i=0
while i<10: #condition acroding to the variable
    L.append(i) # if condition true exciqute part

    i+=1  # loop enisitialazition
print(L)'''

# create a list with wile loop 1 to 1000 in orderd to desinding
'''L=[]
i=1
while i<=100:
    L.append(int(i))
    i+=1

for x in L:
    print (x) # programming paglami'''


#Problem 1 : write a python program to see the multiplication table using wile loop

'''Number=int(input("Enter the number : "))
i=1
while i<=10:
    x=Number*i
    print(Number,"*",i,"=",x)
    i+=1'''
# A name of list you have you have to wish well come everyone wellcom
'''My_list=["Nahid Islam","Mahid Islam","Rohid Sharma","Roni Talukdar"]
for i in My_list:
    print("Wellcome Mr.",i)'''

# using loop to check if the number is prime or not

'''n= int(input("Enter the number : "))
i=2
prime=True
while i<n:
    if n%i==0:
        prime=True
        break
    else:
        prime=False
    i = i+1
if prime:
    print("the number is not prime")
else:
    print("The number is pirme")'''

# wirte to fine the sum of the natural number using looping staracutre
'''n=int(input("Enter the number : "))
Sum=0
while n>=1:
    Sum=Sum+n
    n=n-1
print(Sum)'''

# wirte a python program to get the factorial value to by using for loop

'''n=int(input("Enter the number : "))
Fact=1
if n==0:
    print("Fact is number is : 1")
elif n<0:
      print("Pleace Enter a positive value !")
else:
    for i in range(1,n+1):
        Fact=Fact*i
    print("Fact is number is :",Fact)'''
# wirte a python program to print star diagram

'''n=int(input("Enter the number : "))
m=1
while n>=1:
    print(" "*m, "* "*n)
    m=m+1
    n=n-1
n=int(input("Enter the number : "))
m=1
while n>=1:
    print(" "*n, "* "*m)
    m=m+1
    n=n-1'''
'''n=int(input("Enter the number : "))
for i in range(1,n):
    print(" " * (n-i-1),end=" ")'''

# print squere by star

n=int(input("Enter the number : "))
print ("*  "*n)
m=n-2
while m>=1:
    print("*"," "*((n*2)-1),"*")
    m=m-1
print ("*  "*n)


    

      



    
    






    
    
    
