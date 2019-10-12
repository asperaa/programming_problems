"""Top view of a tree"""
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.hd = 0

class TopView:
    def __init__(self):
        self.maxx = 0
        self.minn = 0
        self.hd_dict = {}
    
    def top_view(self, root):
        if not root:
            return None
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            self.maxx = max(self.maxx, node.hd)
            self.minn = min(self.minn, node.hd)
            if node.hd not in self.hd_dict:
                self.hd_dict[node.hd] = node.val
            if node.left:
                node.left.hd = node.hd - 1
                queue.append(node.left)
            if node.right:
                node.right.hd = node.hd + 1
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
    TV = TopView()

    print(TV.top_view(root))

