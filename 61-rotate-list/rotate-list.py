# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head

        temp = head
        ct = 1
        while temp.next:
            ct+=1
            temp=temp.next
        
        temp.next = head
        numRotations = k%ct
        rangeVal = ct - numRotations
        
        for i in range(rangeVal):
            temp = temp.next
            
        head = temp.next
        temp.next = None

        return head