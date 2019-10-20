"""Given two trees: check if they are identical"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_same(root_a, root_b):
    # base condition if we reach a leaf-end.
    if not root_a and not root_b:
        return True
    # base constion if we reach a leaf-end but one of them is NULL
    if not root_a and root_b or not root_b and root_a:
        return False
    # check if the val of both curr node is same
    if root_a.val == root_b.val:
        # check the left sub-tree and the right-subtree
        left_result = is_same(root_a.left, root_b.left)
        right_result = is_same(root_a.right, root_b.right)
        # if both the sub tree return True then return True otherwise False
        if left_result and right_result:
            return True
        else:
            return False
    # if the node value of both the current nodes is not same return False        
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