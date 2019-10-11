"""Symmetric tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSymmetric(root):
    if root == None:
        return True
    if root.left.val == root.right.val:
        left_check = isSymmetric(root.left)
        right_check = isSymmetric(root.right)
        if left_check and right_check:
            return True
        else:
            return False
    else:
        return False