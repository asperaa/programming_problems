"""Spiral order traversal of the tree"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def spiral_order(root):
    if not root:
        return []
    result = []
    level = []
    spiral = True
    queue = deque()
    queue.append(root)
    while queue:
        count = len(queue)
        for _ in range(count):
            if spiral:
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
        spiral = not spiral
        
        result.append(level)
        level = []
    return result

if __name__ == '__main__': 
    root = TreeNode(1)  
    root.left = TreeNode(2)  
    root.right = TreeNode(3)  
    root.left.left = TreeNode(7)  
    root.left.right = TreeNode(6)  
    root.right.left = TreeNode(5)  
    root.right.right = TreeNode(4)  
    print("Spiral Order traversal of", 
                    "binary tree is ")  
    print(spiral_order(root))

    
