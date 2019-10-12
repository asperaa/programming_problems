"""Left view of the tree"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def left_view(root):
    if not root:
        return root
    result = []
    queue = deque()
    queue.append(root)
    queue.append(None)
    result.append(root.val)

    while queue:

        node = queue.popleft()

        if node:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            if queue:
                result.append(queue[0].val)
                queue.append(None)
    return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(left_view(root))