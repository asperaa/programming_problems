# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    curr_count = 0
    max_count = 0
    prev = None
    result = []

    
    def findMode(self, root):
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if root:
            self.dfs(root.left)
            curr_count = 1 if root.val != self.prev else curr_count + 1
            if curr_count == self.max_count:
                self.result.append(root.val)
            if curr_count > self.max_count:
                self.result = [root.val]
            self.prev = root.val
            self.dfs(root.right)
            