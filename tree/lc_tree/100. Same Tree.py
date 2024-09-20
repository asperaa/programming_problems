# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 and r2:
            return False
        if r1 and not r2:
            return False
        if not r1 and not r2:
            return True
        if r1.val != r2.val:
            return False
        
        is_left_subtree_same = self.isSameTree(r1.left, r2.left)
        is_right_subtree_same = self.isSameTree(r1.right, r2.right)
        return is_left_subtree_same and is_right_subtree_same

