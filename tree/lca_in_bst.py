"""LCA in BST. Time - O(n), Space - O(n2)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bst_search(root, p, q1):
    if root.val == p.val:
        q1.append(root)
        return q1
    elif p.val < root.val:
        q1.append(root)
        q1 = bst_search(root.left, p, q1)
    elif p.val > root.val:
        q1.append(root)
        q1 = bst_search(root.right, p, q1)
    return q1

def lca_in_bst(root, p, q):
    q1 = []
    q2 = []
    q1 = bst_search(root, p, q1)
    q2 = bst_search(root, q, q2)
    lca = root
    for i in range(min(len(q1),len(q2))):
        if q1[i].val == q2[i].val:
            lca = q1[i]
    return lca


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
    print(bst_search(root, TreeNode(7), []))
    print(lca_in_bst(root, TreeNode(0), TreeNode(5)).val)



    