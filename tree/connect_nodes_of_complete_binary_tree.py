"""Connect nodes at the same level of complete binary tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def connect_util(root):
    if not root:
        return None
    if root.left:
        root.left.next = root.right
    if root.right:
        if root.next:
            root.right.next = root.next.left
        else:
            root.right.next = None
    if root.left:
        connect_util(root.left)
    if root.right:
        connect_util(root.right)
    return root
