"""LCA in BT. Iterative."""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(root, p, q):
    stack = []
    stack.append(root)
    parent = {root: None}

    while p not in parent or q not in parent:
        node = stack.pop()

        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    
    while q not in ancestors:
        q = parent[q]
    return q

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

    print(lca(root,root.right.left, root.right.right).val)