"""Symmetric tree. Iterative"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_symmetric(root):
    if not root:
        return True
    
    queue = deque()
    queue.append((root.left, root.right))
    while queue:
        node1, node2 = queue.popleft()
        
        if not node1 and not node2:
            continue
        
        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        queue.append((node1.left, node2.right))
        queue.append((node1.right, node2.left))
    return True

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)

    print(is_symmetric(root))