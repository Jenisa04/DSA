# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        i = 0
        while ptr1:
            ptr1 = ptr1.next
            i+=1
        if i == 1:
            return None
        ptr3 = ptr2 = head
        j = 1
        if i-n == 0:
            ptr2 = ptr2.next
            return ptr2
        else:    
            while j < (i-n) :
                if ptr2.next != None:
                    ptr2 = ptr2.next
                    j+=1
                else:
                    break
            if ptr2.next != None:
                ptr2.next = ptr2.next.next

        return ptr3