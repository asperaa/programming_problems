"""kth smallest element in bst. Space and time - O(h + k) """
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def k_small(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)

    print(k_small(root, 1))