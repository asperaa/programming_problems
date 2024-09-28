# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.inorder_traversal_result = []
        
    def inorder_traversal_helper(self, root):
        if not root:
            return None
        self.inorder_traversal_helper(root.left)
        self.inorder_traversal_result.append(root.val)
        self.inorder_traversal_helper(root.right)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.inorder_traversal_helper(root)
        return self.inorder_traversal_result
        