"""Maximum binary tree. Time complexity - O(n)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_tree_linear(arr):
    stack = []
    last = None
    for num in arr:
        while stack and stack[-1].val < num:
            last = stack.pop()
        node = TreeNode(num)
        if stack:
            stack[-1].right = node
        if last:
            node.left = last
        stack.append(node)
        last = None
    return stack[0]

if __name__  == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    root = max_tree_linear(arr)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.left.right.val, root.left.right.right.val)