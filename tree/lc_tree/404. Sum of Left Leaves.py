# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def sum_of_left_leaves_dfs(self, root, is_left_child):
        if not root:
            return None
        if not root.left and not root.right and is_left_child:
            self.summ += root.val
        else:
            self.sum_of_left_leaves_dfs(root.left, True)
            self.sum_of_left_leaves_dfs(root.right, False)
        return None
        

    
    def sumOfLeftLeaves(self, root):
        self.summ = 0
        if not root:
            return self.summ
        self.sum_of_left_leaves_dfs(root, False)
        return self.summ