# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head is None:
            return head
        
        slow = head
        fast = head
        x = head
        ret = x

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex


        while prev:
            sec = x.next
            x.next = prev
            prev = prev.next
            x.next.next = sec
            x = x.next.next

        


        