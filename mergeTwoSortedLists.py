# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 # Attach l1 to the tail.next
                l1 = l1.next
            else:
                tail.next = l2 # Attach l2 to the tail.next
                l2 = l2.next
        
        # Points to the non empty list 
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next # returns the head of the new list 