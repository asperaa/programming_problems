# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def bst_search_helper(self, root, val):
        if not root:
            return None
        if val > root.val:
            subtree_root = self.bst_search_helper(root.right, val)
        elif val < root.val:
            subtree_root = self.bst_search_helper(root.left, val)
        elif val == root.val:
            subtree_root = root
        return subtree_root

    
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        subtree = self.bst_search_helper(root, val)
        return subtree