"""Serialize and deserialze bt"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return ""
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        node = queue.popleft()

        if not node:
            result.append('None')
        else:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
    return " ".join(result)

def de_serialize(data):
    if not data:
        return None
    
    values = data.split(" ")
    root = TreeNode(int(values[0]))
    queue = deque()
    queue.append(root)
    i = 1
    length = len(values)
    
    while i < length:
        node = queue.popleft()
        if values[i] != "None":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        if values[i] != "None":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    print(serialize(root))
    print(de_serialize(serialize(root)).val)








