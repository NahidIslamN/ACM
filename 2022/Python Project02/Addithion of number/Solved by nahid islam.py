Sum=0
i=int(input("Enter the value of Addition number : "))
if i<0:
    while i<0:
        Sum=Sum+i
        i=i+1
    print("Your Addithon Number is : ",Sum)
else:
    while i>0:
        Sum=Sum+i
        i=i-1
    print("Your Addithon Number is : ",Sum)
