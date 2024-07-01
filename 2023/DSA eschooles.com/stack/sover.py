my_stack = [ ]

def push():
    if len(my_stack)<10:
        a=  int(input("Enter the element : "))
        my_stack.insert(0,a)
    else:
        print("Stack Is full !")
def remove():
    if not my_stack:
        print("Stack is empty !")
    else:
        my_stack.pop(0)
def display():
    if not my_stack:
        print("Stack is Empty !")
    else:
        print(my_stack)
def see_top():
    if not my_stack:
        print("Stack is Empty ! ")
    else:
        print(my_stack[0])

while True:    
    a = int(input("Enter the command,1.push, 2. remove, 3.display, 4.see_top, 5.break : "))
    if a == 1:
        push()
    elif a == 2:
        remove()
    elif a == 3:
        display()
    elif a == 4:
        see_top()
    elif a == 3:
        break
    


            








        
        
