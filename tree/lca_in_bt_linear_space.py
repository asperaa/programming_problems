"""lca in binary tree. Time-O(n) and Space-O(n)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class LCA:
    def __init__(self):
        self.lca = None
    
    def bt_search(self, root, p, q):
        if not root:
            return False
        left = self.bt_search(root.left, p, q)
        right = self.bt_search(root.right, p, q)
        
        if root.val == p.val or root.val == q.val:
            mid = True
        else:
            mid = False
        
        if mid + left + right >= 2:
            self.lca = root
        if mid or left or right:
            return True
        else:
            return False

    
    def lca_search(self, root, p, q):
        self.bt_search(root, p, q)
        return self.lca

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.right = TreeNode(8)
    root.right.left = TreeNode(0)
    lca_obj = LCA()
    print(lca_obj.lca_search(root, TreeNode(5), TreeNode(4)).val)
