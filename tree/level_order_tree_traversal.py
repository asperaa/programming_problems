"""Level order traversal of a tree: Iteration"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(root):
        queue = deque()
        result = []
        queue.append(root)
        queue.append(None)
        sub_result = []

        while queue:
            node = queue.popleft()
            if node:
                sub_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                result.append(sub_result)
                sub_result = []
                if queue:
                    queue.append(None)
            

        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    print(level_order(root))
        