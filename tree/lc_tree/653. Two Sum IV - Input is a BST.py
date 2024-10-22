# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, k, hash_set):
        if not root:
            return
        if k - root.val in hash_set:
            self.ans = True
            return
        hash_set.add(root.val)
        self.dfs(root.left, k, hash_set)
        self.dfs(root.right, k, hash_set)


    def findTarget(self, root, k):
        self.ans = False
        hash_set = set()
        self.dfs(root, k, hash_set)
        return self.ans
