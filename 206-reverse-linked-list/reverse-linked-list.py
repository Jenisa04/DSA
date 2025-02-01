# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #this is the linked list we will return
        curr = head
        while curr:
            # nextNode saves the current pointers next node
            nextNode = curr.next
            # reverses the list
            curr.next = prev
            prev = curr
            curr = nextNode
        
        return prev
 