class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_bfs(root):
    if root:
        queue = []
        queue.append(root)
        
        while(len(queue)!= 0):
            
            tree_node = queue[0]
            print(tree_node.val, end=" ")    
            queue.pop(0)
            
            if tree_node.left is not None:
                queue.append(tree_node.left)
            if tree_node.right is not None:
                queue.append(tree_node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("Level Order Traversal [BFS]:", end= " ")
    level_order_bfs(root)