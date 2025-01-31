# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Jenisa
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mList = dummy = ListNode()

        while(list1 and list2):
            if(list1.val < list2.val):
                mList.next = list1
                mList = list1
                list1 = list1.next

            else:
                mList.next = list2
                mList = list2
                list2 = list2.next
                
        if list1 or list2:
            mList.next = list1 if list1 else list2
        
        
        return dummy.next