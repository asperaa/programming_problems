"""Maximum depth of a binary tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth(root):
    if not root:
        return 0
    left_height = 1 + depth(root.left)
    right_height = 1 + depth(root.right)
    if left_height > right_height:
        return left_height
    else:
        return right_height

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    print(depth(root)) 
