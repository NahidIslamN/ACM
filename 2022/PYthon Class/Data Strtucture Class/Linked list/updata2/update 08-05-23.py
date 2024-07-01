class Node:
        def __init__(self,data):
                self.data=data
                self.next=None

class Linked_List:
        def __init__(self):
                self.head=None
        def add_beg(self,data):
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
        def add_between_a (self,data,X):
                if self.head is None:
                        print("Empty linked List has no attribute to add after")
                else:
                        n=self.head
                        while n is not None:
                                if n.data==X:
                                        break
                                n=n.next
                        if n is None:
                                print("X is not fund to add after X")
                        else:
                                node=Node(data)
                                node.next=n.next
                                n.next=node                        
        def printLL(self):
                if self.head is None:
                        print("Empty Linked List!")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=" ----> ")
                                n=n.next
LL=Linked_List()
LL.add_beg(20)
LL.add_beg(40)
LL.add_beg(50)
LL.add_beg(60)
LL.add_end(75)
LL.add_end(65)
LL.add_between_a (100,40)
LL.add_between_a (200,50)


LL.printLL()
