"""Symmetric tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SymmetricTree:
    def is_symmetric_util(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        
        if root1.val == root2.val:
            left_check = self.is_symmetric_util(root1.left, root2.right)
            right_check = self.is_symmetric_util(root1.right, root2.left)
            if left_check and right_check:
                return True
            else:
                return False
        else:
            return False
    def is_symmetric(self, root):
        return self.is_symmetric_util(root.left, root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(5)
    SymTree = SymmetricTree()
    print(SymTree.is_symmetric(root))