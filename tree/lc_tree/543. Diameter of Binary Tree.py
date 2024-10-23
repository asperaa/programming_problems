# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.dia = 0
    
    
    def dfs(self, root):
        if not root:
            return 0
        l_h = self.dfs(root.left)
        r_h = self.dfs(root.right)
        self.dia = max(self.dia, l_h + r_h)
        return 1 + max(l_h, r_h)
    
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.dfs(root)
        return self.dia
        
