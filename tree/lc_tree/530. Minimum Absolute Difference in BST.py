# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            curr_diff = root.val - self.prev
            self.result = min(self.result, curr_diff)
            self.prev = root.val
            self.dfs(root.right)
            


    def getMinimumDifference(self, root):
        self.result = float('inf')
        self.prev = 0
        self.dfs(root)
        return self.result