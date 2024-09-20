# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    
    def is_symmetric_helper(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 and r2:
            return False
        if r1 and not r2:
            return False
        if r1.val != r2.val:
            return False
        
        return self.is_symmetric_helper(r1.left, r2.right) and self.is_symmetric_helper(r1.right, r2.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.is_symmetric_helper(root.left, root.right)