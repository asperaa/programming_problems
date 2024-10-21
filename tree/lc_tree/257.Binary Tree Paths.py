# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, curr_path):
        if not root:
            return None
        new_node = str(root.val)
        if not root.left and not root.right:
            self.paths.append(curr_path + new_node)
        else:
            self.dfs(root.left, curr_path + new_node + "->")
            self.dfs(root.right, curr_path + new_node + "->")

    
    def binaryTreePaths(self, root):
        if not root:
            return []
        self.paths = []
        self.dfs(root, "")
        return self.paths
        