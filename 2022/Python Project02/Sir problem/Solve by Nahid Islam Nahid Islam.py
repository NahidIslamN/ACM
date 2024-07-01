Sum =int(input("Enter Your Number : "))
B=int(Sum)
if Sum!=B:
    print("Pleace Enter The Right Value")
elif Sum==1:
    print("You are able to drink : 1")
elif Sum==2:
    print("You are able to drink : 3")
else:
    while B>3:
        Sum=Sum+(B/3)
        B=B//3
    print("You are able to drink : ",round(Sum,0)+1)


