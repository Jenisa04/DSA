# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root, 1))
        res = []

        while q:
            n = len(q)
            temp = []
            for _ in range(n):
                node, level = q.popleft()
                if level%2==0:
                    temp.insert(0, node.val)
                else:
                    temp.append(node.val)

                if node.left:
                    q.append((node.left, level+1))
                
                if node.right:
                    q.append((node.right, level+1))

            res.append(temp)

        return res