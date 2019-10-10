"""Check whether the tree is balacned in linear time"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def check_bal_util(root):
    if root == None:
        return (0, True)
    l_height, l_balanced = check_bal_util(root.left)
    r_height, r_balanced = check_bal_util(root.right)
    return max(l_height, r_height) + 1, l_balanced and r_balanced and abs(l_height - r_height) <=1

def check_bal(root):
    return check_bal_util(root)[1]

if __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(4)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.left.left = TreeNode(7)
    print(check_bal(root))
