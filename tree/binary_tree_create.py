# class for an individual node of a binary tree
class Node:
    
    # function to initialise the right and left and key of the node
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# function for inorder traversal
def in_order(root):
    
    # check whether root is None in each recurive call
    if root:
        # recurisive call to the left sub-tree
        in_order(root.left)

        # print the current key
        print(root.key, end=" ")

        # recursive call to the right sub-tree
        in_order(root.right)

# function for pre_order traversal
def pre_order(root):
    # check whether root is None in each recursive call
    if root:
        # print the current key first, then recusive call to the left tree
        print(root.key, end=" ")
        
        pre_order(root.left)
        
        # recursive call to the right tree
        pre_order(root.right)

# function for post_order traversal
def post_order(root):
    # check whether root is None in each recursive call
    if root:
        # recur to the left sub tree, the recur to the right sub tree
        # then print current sub tree
        post_order(root.left)
        post_order(root.right)
        print(root.key, end=" ")


if __name__ == "__main__":

    root = Node(5)
    root.left = Node(4)
    root.right = Node(10)
    root.left.left = Node(2)
    root.left.right = Node(3)

    root.right.left = Node(6)
    root.right.right = Node(12)

    in_order(root)
    print()
    pre_order(root)
    print()
    post_order(root)

    