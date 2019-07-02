# create a class for tree node
class TreeNode:

    # function to create a node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to delete the right most and deepest node
def delete_deep(root, d_node):

    if root is None:
        return
    q = []
    q.append(root)

    while(len(q)):

        temp = q.pop(0)

        if temp is d_node:
            temp = None
            return
        
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


# function to delete the key
def delete_key(root, key):

    if root is None:
        return
    
    q = []
    q.append(root)

    while(len(q)):
        temp = q.pop(0)

        if temp.data == key:
            key_node = temp
        if temp.right:
            q.append(temp.right)
        if temp.left:
            q.append(temp.left)

    x = temp.data
    delete_deep(root, temp)
    key_node.data = x

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

    delete_key(root, 6)

    level_order_bfs(root)