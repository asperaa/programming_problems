"""lca in binary tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bt_search(root, p, q1):
    if root == None:
        return q1
    if root.val == p.val:
        q1.append(root)
        return q1

    bt_search(root.left, p, q1)
    if q1:
        q1.append(root)
    if not q1:
        bt_search(root.right, p, q1)
        if q1:
            q1.append(root)
    return q1

def lca(root, p, q):
    q1 = []
    q2 = []
    q1 = bt_search(root, p, q1)
    q2 = bt_search(root, q, q2)
    lca = root

    for (i, j) in zip(q1[::-1], q2[::-1]):
        if i == j:
            lca = i
    return lca


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
    print(lca(root, TreeNode(5), TreeNode(4)).val)
