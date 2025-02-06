# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists)>1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedList.append(self.merge(l1, l2))
            lists = mergedList

        return lists[0]

    
    def merge(self, list1, list2):
        mList = dummy = ListNode()
        while(list1 and list2):
            if(list1.val < list2.val):
                mList.next = list1
                list1, mList = list1.next, list1

            else:
                mList.next = list2
                list2, mList = list2.next, list2

        if list1 or list2:
            mList.next = list1 if list1 else list2

        return dummy.next