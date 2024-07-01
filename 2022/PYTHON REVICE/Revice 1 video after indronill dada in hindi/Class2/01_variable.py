'''Right way to create a variable
variable এর নাম সবসময় A-Z অথবা ‍a-z দিয়ে শুরু করতে হবে। দুইটি শব্দেরে মাঝখানে স্পেস রাখা যাবে না।
কোন সংখ্যা অথবা কোন সাংক্ষেতিক চিণ্হ দিয়ে ভেরিয়েবলের নাম শুরু করা যাবে না। কোন প্রকার সাংক্ষেতিক চিহ্ণ ভেরিবেয়বললে
নামের সাথে থাকবে না।'''


# Write a python program to add two number
'''a=10
b=20
c=a+b
print(c)'''
# Getting the reminder when a is devided by b
'''a=35
b=10
c=(a%b)
print("The reminder when a is devided by a is : ",c)'''

# input somthein from user check the type of  thes and conver it in intenger
'''a=input("Enter the number")
b=type(a)
print(b)
c=int(a)
print(type(c))'''

# compare two variable and check which one is geter than
'''a=10
b=20
print(a>b)
print(a<b)'''

# Enter 4 number from user and average them
'''a,b,c,d=map(int,input("Enter the numbers : ").split())
average=((a+b+c+d)/4)
print("Average : ",average)'''

'''# Write a python program to calculate squre of a number
a=int(input("Enter the number : "))
B=a*a
print("Squre of thes number is ",B)'''
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
        self.prenext=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_beg(self,data):
        node=Node(data)
        node.next=self.head
        self.head.prenext=node
        self.head=node













