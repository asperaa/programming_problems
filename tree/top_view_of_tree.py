"""Top view of a tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.hd = 0

class TopView:
    def __init__(self):
        self.maxx = 0
        self.minn = 0
        self.hd_dict = {}
    
    def top_view_util(self, root, hd):
        if not root:
            return None
        root.hd = hd
        self.maxx = max(self.maxx, hd)
        self.minn = min(self.minn, hd)
        if hd not in self.hd_dict:
            self.hd_dict[root.hd] = root.val 
        self.top_view_util(root.left, hd - 1)
        self.top_view_util(root.right, hd + 1)
    
    def top_view(self, root):
        self.top_view_util(root, 0)
        result = []
        for i in range(self.minn, self.maxx + 1):
            result.append(self.hd_dict[i])
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    TV = TopView()

    print(TV.top_view(root))

