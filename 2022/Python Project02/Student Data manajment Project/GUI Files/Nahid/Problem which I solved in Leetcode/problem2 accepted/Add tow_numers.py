# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        DH=ListNode(0)
        carry=0
        head=DH
        while l1 or l2:
            if l1:
                val_l1=l1.val
            else:
                val_l1=0
            if l2:
                val_l2=l2.val
            else:
                val_l2=0
            sum_=val_l1+val_l2+carry
            head.next=ListNode(sum_%10)
            head=head.next
            carry=sum_//10
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            head.next=ListNode(carry)
        return DH.next
    

