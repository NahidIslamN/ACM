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
    def print_LL(self):
        if self.head is None:
            print("Linked List is emtpy no item to print")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" >>>>>")
                n=n.next
    def reverseLL(self):
        p=None
        c=self.head
        l=self.head.next
        while c is not None:
            c.next=p
            p=c
            c=l
            if l is not None:
                l=l.next
        if c is None:
            self.head=p
        else:
            pass
            
x=Linked_List()
x.add_beg(45)
x.add_beg(50)
x.add_beg(55)
x.add_beg(65)
#x.reverseLL()
x.print_LL()
