"""Invert a binary tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def invert_tree(root):
    # base case of reaching the children of leaves
    if not root:
        return None
    # temp variable to swap the left and right child of curr root
    temp = root.left
    root.left = root.right
    root.right = temp

    # recursive call for updated left and right child
    invert_tree(root.left)
    invert_tree(root.right)
    return root

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(9)

    root = invert_tree(root)
    print(root.right.right.val) 

