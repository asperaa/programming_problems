"""Serializse and deserialize the bst. Space and Time - O(n)"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root, values):
    if root:
        values.appen(str(root.val))
        preorder(root.left, values)
        preorder(root.right, values)
    return "".join(values)



def serialize(root):

    values = []

    def preorder(root):
        if root:
            values.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
    
    preorder(root)
    return "".join(values)

def de_serialize(values):
    queue = deque(int(data) for data in values.split())
    
    def helper(lower, upper):
        # second condition tells about reaching the leaf node 
        if queue and lower < queue[0] < upper:
            value = queue.popleft()
            node = TreeNode(value)
            node.left = helper(lower, value)
            node.right = helper(value, upper)
            return node
    return helper(float('-inf'), float('inf'))

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    print(serialize(root))
    print(de_serialize(serialize(root)).val)


       