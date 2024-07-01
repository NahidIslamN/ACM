#Add the two number if they polindrome from another....
num1=input("Enter the frist Number : ")
num2=input("Enter the frist Nunber : ")
if num1==num2[::-1]:
    Sum=int(num1)+int(num2)
    print(Sum)
else:
    print("The numbers are not Polindrome from another")
    
#input a Text from user and chek is there "Nahid" present or not
Text=input("Enter your text : ")
if "Nahid" in Text:
    print("Nahid Is present Here")
else:
    print("Nahid is not present Here")
    


        
