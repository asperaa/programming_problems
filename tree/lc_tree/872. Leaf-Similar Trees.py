# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def dfs(self, root, leaves):
        if not root:
            return
        self.dfs(root.left, leaves)
        self.dfs(root.right, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)


    def leafSimilar(self, t1, t2):
        leaves1, leaves2 = [], []
        self.dfs(t1, leaves1)
        self.dfs(t2, leaves2)
        return leaves1 == leaves2
