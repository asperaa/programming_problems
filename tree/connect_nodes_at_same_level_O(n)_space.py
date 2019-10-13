"""Connect nodes at Same level .O(n) space"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def connect_nodes(root):
        if not root:
            return None
        queue = deque()
        queue.append(root)
        queue.append(None)

        while queue:
            node = queue.popleft()
            if node:
                node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                if queue:
                    queue.append(None)
        return root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    connect_nodes(root)
    print(root.left.left.next.val)    