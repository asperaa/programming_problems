"""lca in bst linear space. Time - O(n), O(logn), Space - O(n), O(logn)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(root, p, q):
    if q.val < root.val and p.val < root.val:
        return lca(root.left, p, q)
    elif q.val > root.val and p.val > root.val:
        return lca(root.right, p, q)
    else:
        return root
if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.right.right = TreeNode(9)
    root.right.left = TreeNode(7)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.left = TreeNode(3)
    print(lca(root, TreeNode(0), TreeNode(5)).val)