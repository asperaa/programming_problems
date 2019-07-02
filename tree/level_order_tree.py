# Node class for a tree
class Node:

    # function to initialise the node of the tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to calculate the height of tree
def height(root):
    
    # check if the node is end of leaf (or null)
    if root is None:
        return 0
    # go down the tree recursively to calc height
    else:
        l_height = height(root.left)
        r_height = height(root.right)
        
        # return the larger height
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1

# function to print the given level of binary tree
def print_given_level(root, level):

    if root is None:
        return
    # check if we reached the intended level
    elif level == 1:
        print(root.data, end=" ")
    else:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level -1)

# function to print all the levels
def level_order(root):
    tree_height = height(root)

    for i in range(1, tree_height+1):
        print_given_level(root, i)
        print()

# function to print the all the levels using bfs
def level_order_bfs(root):

    # check if the root is null
    if root is None:
        return
    # create a queue to store the nodes for bfs
    queue = []

    # enqueue the root to the queue
    queue.append(root)
    # iterate until the queue is empty
    while(len(queue) != 0):
   
        print(queue[0].data)
        tree_node = queue.pop(0)

        if tree_node.left is not None:
            queue.append(tree_node.left)
        if tree_node.right is not None:
            queue.append(tree_node.right)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(6)
    root.right = Node(16)
    root.left.left = Node(8)
    root.left.right = Node(9)

    root.right.left = Node(12)
    root.right.right = Node(18)

    level_order(root)
    level_order_bfs(root)