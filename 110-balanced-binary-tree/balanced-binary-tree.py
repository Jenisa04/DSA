# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1

    def height(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        lHt = self.height(node.left)
        if lHt == -1:
            return -1
        
        rHt = self.height(node.right)
        if rHt == -1:
            return -1

        if abs(lHt - rHt) > 1:
            return -1

        return max(lHt, rHt) + 1    