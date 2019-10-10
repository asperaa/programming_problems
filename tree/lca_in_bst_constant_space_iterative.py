"""lca on bst. Itrerative approach"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(root, p, q):
    node = root
    while node:
        if q.val < node.val and p.val < node.val:
            node = node.left
        elif q.val > node.val and p.val > node.val:
            node = node.right
        else:
            return node

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

