class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    #add data in begining in a linked list    
    def add_begning(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    #add data at the end of a linked list
    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=node
    # traversel operation of a linked list 
    def show_data(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            n=self.head
            while n is not None:
                print(n.data,"----->",end=" ")
                n=n.next
L=LinkedList()            
while True:
    choice=input("Enter the choice : ")
    
    if choice=="add data":
        x=input("enter element : ")
        L.add_begning(x)
    elif choice=="show data":
        L.show_data()
    elif choice=="add end":
        x=input("enter element : ")
        L.add_end(x)
        
    elif choice=="exit":
        break
    else:
        print(choice,"is not define ! make sure it a true instracsion")
        
