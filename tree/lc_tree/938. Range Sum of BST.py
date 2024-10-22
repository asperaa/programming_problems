# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def search_and_add(self, root, L, R):
        if not root:
            return
        if root.val >= L and root.val <= R:
            self.summ += root.val
        if root.val < L:
            self.search_and_add(root.left, L, R)
        if root.val > R:
            self.search_and_add(root.right, L, R)
            
    

    
    def rangeSumBST(self, root, L, R):
        self.summ = 0
        self.search_and_add(root, L, R)
        return self.summ
