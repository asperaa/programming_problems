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

def min_value_node(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def delete_node(root, key):

    if root is None:
        return root
    
    if key > root.data:
        root.right = delete_node(root.right, key)
    elif key < root.data:
        root.left = delete_node(root.left, key)
    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            min_node = min_value_node(root.right)
            root.data = min_node.data
            root.right = delete_node(root.right, min_node.key)
    return root

if __name__ == "__main__":

    root = Node(50)
    insert(root, 30) 
    insert(root, 20) 
    insert(root, 40) 
    insert(root, 70) 
    insert(root, 60) 
    insert(root, 80)

    in_order(root)
    root = delete_node(root, 80)
    print()
    in_order(root)
