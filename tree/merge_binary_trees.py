"""Merge bibary trees"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def merge_tree(root1, root2):
    if not root1 and not root2:
        return None
    if root1 and root2:
        new_root = TreeNode(root1.val + root2.val)
        new_root.left = merge_tree(root1.left, root2.left)
        new_root.right = merge_tree(root1.right, root2.right)
    elif root1 and not root2:
        new_root = TreeNode(root1.val)
        new_root.left = merge_tree(root1.left, root2)
        new_root.right = merge_tree(root1.right, root2)
    elif root2 and not root1:
        new_root = TreeNode(root2.val)
        new_root.left = merge_tree(root1, root2.left)
        new_root.right = merge_tree(root1, root2.right)
    return new_root

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    # root1.right = TreeNode(3)

    root2 = TreeNode(4)
    root2.left = TreeNode(5)
    root2.right = TreeNode(6)

    result_root = merge_tree(root1, root2)
    print(result_root.right.val) 