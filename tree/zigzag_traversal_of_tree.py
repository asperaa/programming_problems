"""Zigzag traversal of tree"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    
def zigzag(root):
    if not root:
        return root
    result = []
    level = []
    queue = deque()
    queue.append(root)
    zigzag = False

    while queue:
        count = len(queue)
        for _ in range(count):
            if zigzag:
                node = queue.pop()
                level.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
            else:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        result.append(level)
        zigzag = not zigzag
        level = []
    return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(zigzag(root))

        
        