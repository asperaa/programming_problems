class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, data):
    
    if root is None:
        return
    
    tree_node = TreeNode(data)

    queue = []
    # initialise the queue for bfs (with root node) [not the val of root]
    queue.append(root)
    
    # start the bfs
    while(len(queue)):
        # pop node from front of queue and explore left and right neighbours of the node
        node = queue.pop(0)

        # if the left neighbour is null, then add the node there   
        if node.left is None:
            node.left = tree_node
            break
        # or else continue the adding neighbours in the queue for bfs
        else:
            queue.append(node.left)
        
        # if the right neighbour is null, then add the node there
        if node.right is None:
            node.right = tree_node
            break
        # or else continue the adding of neighbours in the queue for bfs
        else:
            queue.append(node.right)

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
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(16)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(9)

    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    level_order_bfs(root)

    insert_node(root, 90)

    level_order_bfs(root)