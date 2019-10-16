"""All nodes dist k in BT"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class KNodeDist:
    def __init__(self):
        self.k_dist_nodes = []
        self.target_node = None
        self.parent = dict()
        self.path = dict()
        
    
    def search(self, root, target, depth):
        if not root:
            return None
        if root.val == target:
            self.target_node = root
            self.target_root_dist = depth
        if root.left:
            self.parent[root.left] = root
        if root.right:
            self.parent[root.right] = root

        self.search(root.left, target, depth + 1)
        self.search(root.right, target, depth + 1)
    
    
    def lower_nodes(self, root, depth, target, k):
        if not root:
            return None
        if root in self.path:
            return None
        if depth == k:
            self.k_dist_nodes.append(root.val)
        self.lower_nodes(root.left, depth+1, target, k)
        self.lower_nodes(root.right, depth+1, target, k)
    
    def k_dist(self, root, target, k):
        if not root:
            return []
        self.original_k = k
        self.parent[root] = None
        self.search(root, target, 0)
        parent_node = self.target_node
        while parent_node and k != -1:
            
            self.lower_nodes(parent_node, 0, target, k)
            self.path[parent_node] = True
            parent_node = self.parent[parent_node]
            k = k - 1
        return self.k_dist_nodes

if __name__ == "__main__":
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(5)
    # root.left.left.left = TreeNode(6)
    # root.right.left = TreeNode(8)
    # root.right.right = TreeNode(7)
    # root.left.right = TreeNode(10)
    # root.left.right.right = TreeNode(11)
    # root.left.right.left = TreeNode(15)
    # root.left.right.right.left = TreeNode(17)
    # root.left.right.right.right = TreeNode(13)
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    # root.left.left.left = TreeNode(6)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right = TreeNode(10)
    root.left.right.right = TreeNode(4)
    root.left.right.left = TreeNode(7)
    # root.left.right.right.left = TreeNode(17)
    # root.left.right.right.right = TreeNode(13)
    KNodeDist = KNodeDist()
    print(KNodeDist.k_dist(root, 5, 2))
