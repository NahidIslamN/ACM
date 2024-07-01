class Node:
        def __init__(self, data):
                self.data=data
                self.next=None
class LinkedList:
        def __init__(self):
                self.head=None
        def add_beg (self,data):
                node=Node(data)
                node.next=self.head
                self.head=node
        def add_end(self,data):
                node=Node(data)
                if self.head is None:
                        node.next=self.head
                        self.head=node
                else:
                        n=self.head
                        while n.next is not None:
                                n=n.next
                        n.next=node
        def add_between_a (self,data,X):
                if self.head is None:
                        print("Empty Linked List")
                else:
                        n=self.head
                        while n is not None:
                                if n.data==X:
                                        break
                                n=n.next
                        if n is None:
                                print("X is not found")
                        else:
                                node=Node(data)
                                node.next=n.next
                                n.next=node
        def add_between_a (self,data,X):
                if self.head is None:
                        print("Empty Linked List")
                        return
                if self.head.data == X:
                        node=Node(data)
                        node.next=self.head
                        self.head=node
                        return
                else:
                        n=self.head
                        while n.next is not None:
                                if n.next.data==X:
                                        break
                                n=n.next
                        if n.next is None:
                                print("X is not found")
                        else:
                                node=Node(data)
                                node.next=n.next
                                n.next=node

                                
                        
                        
           
        def printLL(self):
                if self.head is None:
                        print("Empty Linked List")
                else:
                        n=self.head
                        while n is not None:
                                print(n.data,end=" ------> ")
                                n=n.next
LL=LinkedList()

LL.add_end(35)
LL.add_end(40)
LL.add_beg(75)
LL.add_between_a (30,75)
LL.add_between_a(46,40)
LL.add_between_a (40,30)
LL.add_between_a (45,30)
LL.printLL()
