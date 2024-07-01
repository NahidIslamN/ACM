class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List:
    def __init__(self):
        self.head=None
    def add_begining(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node
    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=node
    def add_between_a(self,data,x):
        if self.head is None:
            print("Linked List is empty X is not Found")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.next
            if n is None:
                print("X is not found")
            else:
                node=Node(data)
                node.next=n.next
                n.next=node
    def add_between_b(self,data,x):
        if self.head is None:
            print("Linked List is empty, x is not found")
        else:
            if self.head.data ==x:
                node=Node(data)
                node.next=self.head
                self.head=node
            else:
                n=self.head
                while n is not None:
                    if n.next.data==x:
                        break
                    n=n.next
                if n is None:
                    print("X is not found")
                else:
                    node=Node(data)
                    node.next=n.next
                    n.next=node
    def addifempty(self,data):
        if self.head is not None:
            print("Linked List is full, can't implement item here")
        else:
            node=Node(data)
            node.next=self.head
            self.head=node
    def delete_beg(self):
        if self.head is None:
            print("Empty Linked has not any value to delete")
        else:
            self.head=self.head.next
    def delete_end(self):
        if self.head is None:
            print("Empty Linked has not any value to delete")
        elif self.head.next is None:
            self.head=None
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None                 
    def printLL(self):
        if self.head is None:
            print("Linked List is empty !")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ----> ")
                n=n.next
    def delete_any(self,x):
        if self.head is None:
            print("Linked List is empty!")
        elif self.head.data ==x:
            self.head=self.head.next
        else:
            n=self.head
            while n.next is not None:
                if n.next.data==x:
                    break
                n=n.next
            if n.next is None:
                print("x is not found")
            else:
                n.next=n.next.next
LL=Linked_List ()
LL.addifempty(25)
LL.add_begining(45)
LL.add_end(74)
LL.delete_any(75)


LL.printLL()
