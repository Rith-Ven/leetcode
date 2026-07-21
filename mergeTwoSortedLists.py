# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # To avoid edge case of inserting into empty list
        tail = dummy

        while l1 and l2: # Ensures lists are not null
            if l1.val < l2.val: # Point to smaller val
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:          # attach remainder of sorted list to end of tail
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next # head of new list