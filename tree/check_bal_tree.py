"""check if the tree is balanced. Time-O(n2)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if not root:
        return 0
    return max(1+ height(root.left), 1 + height(root.right))

def check_bal(root):

    if not root:
        return True
    l_height = height(root.left)
    r_height = height(root.right)
    if abs(l_height - r_height) <=1:
        l_check = check_bal(root.left)
        r_check = check_bal(root.right)
        if l_check and r_check:
            return True
        else:
            return False
    else:
        return False




if __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(4)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    # root.left.left.left = TreeNode(7)
    print(check_bal(root))
