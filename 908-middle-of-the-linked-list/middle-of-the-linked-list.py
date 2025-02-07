# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = ptr2 = head
        
        while(ptr2 != None and ptr2.next != None):
            ptr2 = ptr2.next.next   #takes 2 steps at a time
            ptr1 = ptr1.next        #takes 1 step at a time

        return ptr1