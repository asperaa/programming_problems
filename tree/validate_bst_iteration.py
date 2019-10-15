"""Validate a bst using iteration"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_bst(root):
    if not root:
        return True
    
    stack = [(root, float('-inf'), float('inf')),]
    while stack:
        node, lower, upper = stack.pop()
        if not node:
            continue
        val = node.val
        
        if val <= lower or val >= upper:
            return False

        stack.append((node.right, val, upper))
        stack.append((node.left, lower, val))
    
    return True

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(1)
    root.right = TreeNode(18)
    # root.right.left = TreeNode(11)

    print(is_bst(root))