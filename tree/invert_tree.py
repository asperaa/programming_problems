"""Invert a binary tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def invert_tree(root):


    if root.left and root.right:
        temp = root.left
        root.left = root.right
        root.right = temp
        invert_tree(root.left)
        invert_tree(root.right)
    elif root.left and not root.right:
        temp = root.left
        root.left = root.right
        root.right = temp
        invert_tree(root.right)
    elif root.right and not root.left:
        temp = root.left
        root.left = root.right
        root.right = temp
        invert_tree(root.left)
    return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    # root.right = TreeNode(7)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(9)

    root = invert_tree(root)
    print(root.right.val) 

