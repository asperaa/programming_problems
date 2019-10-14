"""Root to leaf path sum"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class PathSum:
    def __init__(self):
        self.is_sum = False
    
    def path_sum_util(self, root, summ, r_sum):
        if not root:
            return None
        r_sum += root.val
        if not root.left and not root.right:
            if summ == r_sum:
                self.is_sum = True
                return None
        self.path_sum_util(root.left, summ, r_sum)
        self.path_sum_util(root.right, summ, r_sum)

    def path_sum(self, root, summ):
        if not root:
            return self.is_sum

        self.path_sum_util(root, summ, 0)
        return self.is_sum

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    PS = PathSum()
    print(PS.path_sum(root, 21))