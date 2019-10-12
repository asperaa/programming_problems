"""Bottom view of the tree"""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BottomView:
    def __init__(self):
        self.hd_dict = {}
        self.maxx = 0
        self.minn = 0
        self.node_hd = {}
    
    def bottom_view(self, root):
        if not root:
            return None
        
        result = []
        queue = deque()
   
        queue.append(root)
        self.node_hd[root] = 0     
        while queue:
            node = queue.popleft()

            self.hd_dict[self.node_hd[node]] = node.val

            self.maxx = max(self.maxx, self.node_hd[node])
            self.minn = min(self.minn, self.node_hd[node])
            
            if node.left:
                self.node_hd[node.left] = self.node_hd[node] - 1
                queue.append(node.left)
            if node.right:
                self.node_hd[node.right] = self.node_hd[node] + 1
                queue.append(node.right)
        
        for i in range(self.minn, self.maxx + 1):
            result.append(self.hd_dict[i])
        return result

    

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.right = TreeNode(6)
    root.left.right.right.right.right = TreeNode(7)
    BV = BottomView()

    print(BV.bottom_view(root))