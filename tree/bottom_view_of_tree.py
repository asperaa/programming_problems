"""Bottom view of the tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BottomView:
    def __init__(self):
        self.hd_dict = {}
        self.maxx = 0
        self.minn = 0
        self.node_hd = {}
    
    def bottom_view_util(self, root, hd):
        if not root:
            return None
        self.node_hd[root] = hd
        self.maxx = max(self.maxx, hd)
        self.minn = min(self.minn, hd)
        if hd not in self.hd_dict:
            self.hd_dict[hd] = [root.val]
        else:
            self.hd_dict[hd].append(root.val)
        self.bottom_view_util(root.left, hd - 1)
        self.bottom_view_util(root.right, hd + 1)
    
    def bottom_view(self, root):
        self.bottom_view_util(root, 0)
        result = []
        for i in range(self.minn, self.maxx + 1):
            print(self.hd_dict[i])
            result.append(self.hd_dict[i][-1])
        return result
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.right = TreeNode(6)
    root.left.right.right.right.right = TreeNode(7)
    BV = BottomView()

    print(BV.bottom_view(root))