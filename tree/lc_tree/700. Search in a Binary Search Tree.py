# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def search_bst_helper(self, root, val, subtree_root):
        if not root:
            return
        if val < root.val:
            self.search_bst_helper(root.left, val, subtree_root)
        elif val > root.val:
            self.search_bst_helper(root.right, val, subtree_root)
        else:
            subtree_root = root
            return
    
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.subtree_root = None
        self.search_bst_helper(root, val, self.subtree_root)
        return self.subtree_root
        