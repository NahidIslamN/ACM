class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_begening(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def printLLI(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
LL=LinkedList()
LL.add_begening([10,42,52,65])
LL.add_begening([10,45,55,65])
LL.add_begening([15,46,52,100])
LL.add_begening([15,48,59,65])
LL.add_begening([200,125,75,65])
LL.add_begening([101,42,500,200])
LL.printLLI()
        
