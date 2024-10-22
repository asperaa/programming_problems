# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, vals):
        if root:
            vals.append(root.val)
            self.dfs(root.left)
            self.dfs(root.right)
            
    def isUnivalTree(self, root):
        if not root:
            return True
        
        self.vals = []
        self.dfs(root, self.vals)
        return len(set(self.vals)) == 1