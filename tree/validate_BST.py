"""Validate BST"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_bst_util(root, lower_limit, upper_limit):
    if not root:
        return True
    val = root.val
    if val <= lower_limit or val >= upper_limit:
        return False
    r_bst = is_bst_util(root.right, val, upper_limit)
    if not r_bst:
        return False
    
    l_bst = is_bst_util(root.left, lower_limit, val)
    if not l_bst:
        return False

    return True

def is_bst(root):

    lower = float('-inf')
    upper = float('inf')
    return is_bst_util(root, lower, upper)

    
    

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(1)
    root.right = TreeNode(8)
    root.right.left = TreeNode(4)

    print(is_bst(root))


