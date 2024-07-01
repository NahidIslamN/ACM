class Node:
    def __init__(self,data):
        self.data=data
        self.anext=None
        self.pnext=None
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
    def add_bet_ax(self,data,x):
        if self.head is None:
            print("Linked List is empty! x is not found")
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
                if n.anext is not None: 
                    node.anext=n.anext
                    node.pnext=n
                    n.anext.pnext=node
                    n.anext=node
                else:
                    n.anext=node
                    node.pnext=n
    def add_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.anext is not None:
                n=n.anext
            node.pnext=n
            n.anext=node
    def add_bet_bx(self,data,x):
        if self.head is None:
            print("Linked List is empty! x is not found to add item")
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
                print("x is not found")
            else:
                node=Node(data)
                node.anext=n.anext
                n.anext.pnext=node
                n.anext=node
                node.pnext=n
                
        
    def show_node_fd(self):
        if self.head is None:
            print("Linked List is empty! No item to print")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" >>>>> ")
                n=n.anext
    def show_node_bd(self):
        if self.head is None:
            print("Linked List is empty! No item to print")
        else:
            n=self.head
            while n.anext is not None:
                n=n.anext
            while n is not None:
                print(n.data,end=" >>>>> ")
                n=n.pnext
LL=DLinked_List()
LL.add_end(75)
LL.add_beg(85)
LL.add_beg(45)
LL.add_beg(55)
LL.add_end(100)
LL.add_beg(459)
LL.add_bet_ax(56,45)
LL.add_bet_bx(105,100)
LL.show_node_fd()
        
