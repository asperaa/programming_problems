"""Determine whether the tree is complete binary tree or not"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_cbt(root):
    if not root:
        return True
    queue = deque()
    queue.append(root)
    flag  = False

    while queue:
        node = queue.popleft()
        if not node:
            flag = True
        else:
            if flag:
                return False
            queue.append(node.left)
            queue.append(node.right)
    
    return True
    
    


    


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.right.right = TreeNode(7)
    print(is_cbt(root))
