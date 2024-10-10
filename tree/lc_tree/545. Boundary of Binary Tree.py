# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.result = []
        
        
    def left_traversal(self, root):
        if not root:
            return None
        if root.left:
            self.result.append(root.val)
            self.left_traversal(root.left)
        elif root.right:
            self.result.append(root.val)
            self.left_traversal(root.right)
    
    def right_traversal(self, root):
        if not root:
            return None
        if root.right:
            self.result.append(root.val)
            self.right_traversal(root.right)
        elif root.left:
            self.result.append(root.val)
            self.right_traversal(root.left)
            
    def leaf_traversal(self, root):
        if not root:
            return None
        
        if not root.right and not root.left:
            self.result.append(root.val)
        
        self.leaf_traversal(root.left)
        self.left_traversal(root.right)
    
            
        
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.result.append(root.val)
        self.left_traversal(root.left)
        self.leaf_traversal(root.left)
        self.leaf_traversal(root.right)
        self.right_traversal(root.right)

        