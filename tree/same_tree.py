"""Given two trees: check if they are identical"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_same(root_a, root_b):
    if not root_a and not root_b:
        return True
    if not root_a and root_b or not root_b and root_a:
        return False
    if root_a.val == root_b.val:
        left_result = is_same(root_a.left, root_b.left)
        right_result = is_same(root_a.right, root_b.right)

        if left_result and right_result:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    root_a = TreeNode(1)
    root_b = TreeNode(1)

    root_a.left = TreeNode(2)
    root_b.left = TreeNode(2)

    root_a.right = TreeNode(3)
    root_b.right = TreeNode(3)

    print(is_same(root_a, root_b))