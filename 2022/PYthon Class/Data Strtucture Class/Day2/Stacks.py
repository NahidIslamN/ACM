Stack=[]
def push():
    element=input("Enter the element : ")
    Stack.append(element)
    print(Stack)
def pop():
    if not Stack:
        print("Strack is empty")
    else:
        e=Stack.pop()
        print("The remove item is : ",e)
while True:
    choice=int(input("Enter the choce to push (1), to pop(2) and to quite(3) : "))
    if choice ==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("press enter to connect the function")
        
        
