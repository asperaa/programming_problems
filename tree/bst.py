class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(root, key):

    if root is None or root.data == key:
        return root
    
    if key > root.data:
        return search(root.right, key)
    return search(root.left, key)

def insert(root, key):

    tree_node = Node(key)

    if root is None:
        return root
    else:
        if key > root.data:
            if root.right is None:
                root.right = tree_node
            else:
                insert(root.right, key)
        else:
            if root.left is None:
                root.left = tree_node
            else:
                insert(root.left, key)  

def in_order(root):

    if root is not None:
        in_order(root.left)
        print(root.data)
        in_order(root.right)

if __name__ == "__main__":

    root = Node(50)
    insert(root, 30) 
    insert(root, 20) 
    insert(root, 40) 
    insert(root, 70) 
    insert(root, 60) 
    insert(root, 80)

    in_order(root)

