class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printLL(self):
        if self.head is None:
            print("Linked list is empty! not item to print")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" >>>>> ")
                n=n.ref
    def add_beg(self,data):
        node=Node(data)
        node.ref=self.head
        self.head=node

    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=node
    def add_bet_ax (self,data,x):
        if self.head is None:
            print("Linked List is empty x is not found")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.ref
            if n is None:
                print("x is not found")
            else:
                node=Node(data)
                node.ref=n.ref
                n.ref=node
    def add_bet_bx(self,data,x):
        if self.head is None:
            print("Linked List is empty x is not found")
        elif self.head.data==x:
            node=Node(data)
            node.ref=self.head
            self.head=node
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("x is not found")
            else:
                node=Node(data)
                node.ref=n.ref
                n.ref=node
    def delete_item_begining(self):
        if self.head is None:
            print("Linked List is empty! No item found to delete")
        else:
            self.head=self.head.ref
    def delete_item_end(self):
        if self.head is None:
            print("Linked List is empty! No item found to delete")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_any_item(self,x):
        if self.head is None:
            print(" Linked List is empty, x is not found")
        elif self.head.data==x:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("x is not found to delete")
            else:
                n.ref=n.ref.ref
                
                
                
LL=LinkedList()
LL.add_beg(25)
LL.add_end(22)
LL.add_bet_ax(26,25)
LL.add_bet_ax(35,26)
LL.add_bet_bx(27,26)
LL.delete_item_begining()
LL.delete_item_end()
LL.delete_any_item(27)
LL.printLL()
            
                
    
