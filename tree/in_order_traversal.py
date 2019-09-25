"""In order traversal in a tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order(root):
    if not root:
        return None
    in_order(root.left)
    print(root.val)
    in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    in_order(root)
