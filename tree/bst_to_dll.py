"""bst to dll (doubl linked list). Time and Space: O(n)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def bst_to_dll(root):
    dummy = TreeNode(0)
    prev = dummy
    stack = []
    node = root
    while stack or node:

        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        node.left = prev
        prev.right = node
        prev = node
        node = node.right
    
    dummy.right.left = prev
    prev.right = dummy.right

    return dummy.right

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    print(bst_to_dll(root).right.right.right.val) # should print 2
        