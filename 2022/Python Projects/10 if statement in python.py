# ---- Chepter 9  If State ment in python----------------

# If statement syntax

# if (condition):
        #if body
#else:
    #else body


#a =int(input("Enter the value of A = "))
#b=int(input("Enter the value of B = "))
#c=int(input("Enter the value of C = "))
#if(a>b)and (a>c):
#    print("The largest value is A : ",a)
#elif (b>a) and (b>c):
#    print("The largest value is B : ",b)
#elif (c>a) and (c>b):
#    print("The largest value is C : ",c)
#else:
#    print("Please Insert the right Value")




# Program to find out the user is eligible ofr driving licence :==================

#Driver_age = int(input("Enter your driver age : "))

#if Driver_age>=18 and Driver_age<=45 : 
#    print("Your Cliend is elegible for geting a driving licence")
#elif Driver_age<18:
#    print("Your cliend is too young........ Try after 18 years old")
#else:
#    print("You Cliend is too old..........! Couldn't get a driving licence")




# Program to find out the user of phone number is GP or Robi or Teletalk

#Phone_Number= str(input("Enter yoru Phone Number : "))
#if  len(Phone_Number)>11:
#    print("Enter a vaild Phone number")
#elif Phone_Number[0:3]=="017":
#    print('''You are GP user
#     Your Phone Number is : ''',Phone_Number)
#elif Phone_Number[0:3]=="013":
#    print('''You are GP user
#     Your Phone Number is : ''',Phone_Number)
#elif Phone_Number[0:3]=="018":
#    print('''You are Robi User
#    Your phone Number is : ''',Phone_Number)
#elif Phone_Number[0:3]=="015":
#    print('''You are Teletalk User 
#    Your phone Number is : ''',Phone_Number)
#elif Phone_Number[0:3]=="019":
#    print('''You are Banglalink User 
#    Your phone Number is : ''',Phone_Number)
#else:
#    print("Enter a vaild Phone number!!!!!")
