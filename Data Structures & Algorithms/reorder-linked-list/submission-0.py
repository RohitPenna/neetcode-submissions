# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        one = head
        two = head
        counter = 0

        while two and two.next:
            one = one.next
            two = two.next.next
            counter += 1
        

        start = one.next
        one.next = None
        prev = None

        while start:
            nextNode = start.next
            start.next = prev
            prev = start
            start = nextNode

        first = head          
        second = prev 

        while second:
            fnext = first.next
            snext = second.next

            first.next = second
            second.next = fnext

            first = fnext
            second = snext


        
        