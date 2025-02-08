# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = head       
        while head.next:
            print(head.val)
            if head.val == head.next.val:
                temp = head.next
                head.next = temp.next
                temp.next = None
                if head.next:
                    if head.val != head.next.val:
                        head = head.next
                    else:
                        continue
                else:
                    break
            else:
                if head.next:
                    head=head.next
                
        return dummy