# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val <= list2.val:
            place = list1
            list1 = list1.next
        else:
            place = list2
            list2 = list2.next
        
        x = place

        end = True
        
        while place:
            if list1 is None:
                end = False
                while list2:
                    place.next = list2
                    list2 = list2.next
                    place = place.next
                    break
            
            if list2 is None:
                end = False
                while list1:
                    place.next = list1
                    list1 = list1.next
                    place = place.next
                    break

            if end:
                if list1.val <= list2.val:
                    place.next = list1
                    list1 = list1.next
                else:
                    place.next = list2
                    list2 = list2.next
            else:
                break

            place = place.next

        return x