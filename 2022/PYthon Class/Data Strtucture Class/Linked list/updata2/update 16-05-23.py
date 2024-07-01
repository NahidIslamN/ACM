class Node:
    def __init__(self,data):
        self.data=data
        self.pnext=None
        self.anext=None
class DLinked_List:
    def __init__(self):
        self.head=None
    def add_beg(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.anext=self.head
            self.head.pnext=node
            self.head=node
    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.anext is not None:
                n=n.anext
            n.anext=node
            node.pnext=n
    def add_bet_ax(self,data,x):
        if self.head is None:
            print("Linked List is empty! x is not found to add item")
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.anext
            if n is None:
                print("x is not found")
            else:
                node=Node(data)
                if n.anext is None:
                    n.anext=node
                    node.pnext=n
                else:
                    node.anext=n.anext
                    n.anext.pnext=node
                    n.anext=node
                    node.pnext=n

    def add_bet_bx(self,data,x):
        if self.head is None:
            print("Linked List is empty! x is not found to print")
        elif self.head.data==x:
            node=Node(data)
            node.anext=self.head
            self.head.pnext=node
            self.head=node
        else:
            n=self.head
            while n.anext is not None:
                if n.anext.data==x:
                    break
                n=n.anext
            if n.anext is None:
                print("Linked List is empty! x is not found to add data")
            else:
                node=Node(data)
                node.anext=n.anext
                n.anext.pnext=node
                n.anext=node
                node.pnext=n
    def printLL_fd(self):
        if self.head is None:
            print("Linked List is empty! not item to print")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" >>>>> ")
                n=n.anext
    def printLL_bd(self):
        if self.head is None:
            print("Linked List is empty! not item to print")
        else:
            n=self.head
            while n.anext is not None:
                n=n.anext
            while n is not None:
                print(n.data,end=" >>>>> ")
                n=n.pnext
                
            
LL=DLinked_List()
LL.add_beg(10)
LL.add_beg(20)
LL.add_end(75)
LL.add_bet_ax(25,20)
LL.add_bet_bx(85,75)
LL.printLL_fd()
