"""Maximum binary tree. Time complexity - O(n)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_tree_linear(arr):
    # maintain a stack which always has nums in descending order
    # (bottom of stack will have largest number)
    stack = []
    # this will store the element that should be left of the root
    last = None
    # iterate the array from left to right
    for num in arr:
        # pop the elements from stack which are smaller than the current array
        while stack and stack[-1].val < num:
            last = stack.pop()
        # make tree-node fomr curr number
        node = TreeNode(num)
        # assign the right child of top node in stack
        if stack:
            stack[-1].right = node
        # assign the left node of the curr node (curr num in the array)
        if last:
            node.left = last
        # append the curr node
        stack.append(node)
        # reset the last pointer
        last = None
    # in the end the stack will have the largest number of the array (which is root of the built tree)
    return stack[0]

if __name__  == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    root = max_tree_linear(arr)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.left.right.val, root.left.right.right.val)