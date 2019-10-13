"""Connect nodes of tree in constant space"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    original_root = root
    tail = TreeNode(0)
    dummy = tail
    while root:
        tail.next = root.left
        if tail.next:
            tail = tail.next
        tail.next = root.right
        if tail.next:
            tail = tail.next
        root = root.next
        if root == None:
            tail = dummy
            root = dummy.next
    return original_root

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    connect(root)
    print(root.left.left.next.val) 

        