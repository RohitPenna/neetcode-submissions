# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        total = 0

        x = ListNode(0)
        ret = x

        while l1 or l2:
            
            if not l2:
                total = l1.val + carry
            elif not l1:
                total = l2.val + carry
            else:
                total = l2.val + l1.val + carry
            
            carry = 0
            
            if total >= 10:
                carry += 1
                total -= 10
            
            x.next = ListNode(total)
            x = x.next
            if l1 and l1.next:
                l1 = l1.next
            else:
                l1 = None
            if l2 and l2.next:
                l2 = l2.next 
            else:
                l2 = None
        
        if carry > 0:
            x.next = ListNode(carry)

        return ret.next

