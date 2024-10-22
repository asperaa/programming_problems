# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_same_tree(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 and t2:
            return False
        if t1 and not t2:
            return False
        return self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right)

    
    def sub_tree_helper(self, t1, t2):
        if not t1 or not t2:
            return
        if t1.val == t2.val:
            self.subtree = self.subtree or self.is_same_tree(t1, t2)
        self.sub_tree_helper(t1.left, t2)
        self.sub_tree_helper(t1.right, t2)
        

    def isSubtree(self, t1, t2):
        self.subtree = False
        self.sub_tree_helper(t1, t2)
        return self.subtree
