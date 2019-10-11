"""Diameter of a tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Dia:
    def __init__(self):
        self.ans = 0

    def diameter_util(self, root):
        if not root:
            return 0
        l_height = self.diameter_util(root.left)
        r_height = self.diameter_util(root.right)
        self.ans = max(self.ans, l_height + r_height)
        return max(l_height, r_height) + 1
    
    def diameter(self, root):
        self.diameter_util(root)
        return self.ans
   

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    Dia = Dia()
    print(Dia.diameter(root))