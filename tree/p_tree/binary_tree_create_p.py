#I'm the captain of my ship

class Node:
    
    def __init__(self, val):
        
        self.val = val
        self.left = None
        self.right = None

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=" ")
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.val, end=" ")
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=" ")


if __name__ == "__main__":
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("Inorder Traversal:", end=" ")
    in_order(root)
    print()
    
    print("Pre Order Traversal:", end=" ")
    pre_order(root)
    print()
    
    print("Post Order Traversal:", end=" ")
    post_order(root)
    print()
    
    
            