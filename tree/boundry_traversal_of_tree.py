"""Boundry Traversal of a tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BoundryTraversal:
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
            self.right_traversal(root.right)
            self.result.append(root.val)
        elif root.left:
            self.right_traversal(root.left)
            self.result.append(root.val)
    
    def leaf_traversal(self, root):
        if not root:
            return None
        if not root.right and not root.left:
            self.result.append(root.val)
        self.leaf_traversal(root.left)
        self.leaf_traversal(root.right)
    
    def boundry_traversal(self, root):
        if not root:
            return []
        self.result.append(root.val)
        self.left_traversal(root.left)
        self.leaf_traversal(root.left)
        self.leaf_traversal(root.right)
        self.right_traversal(root.right)
        return self.result
        
    
if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    BT = BoundryTraversal()
    print(BT.boundry_traversal(root))
    print(BT.result)
