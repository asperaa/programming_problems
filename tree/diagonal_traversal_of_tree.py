"""Diagonal traversal of tree"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class DiagonalTraversal:
    def __init__(self):
        self.slope_dict = dict()

    def diagonal_util(self, root, d):
        if not root:
            return None
        if d in self.slope_dict:
            self.slope_dict[d].append(root.val)
        else:
            self.slope_dict[d] = [root.val]
        if root.left:
            self.diagonal_util(root.left, d+1)
        if root.right:
            self.diagonal_util(root.right, d)

    def diagonal_traversal(self, root):
        if not root:
            return []
        self.diagonal_util(root, 0)
        result = []
        for i in self.slope_dict:
            result.append(self.slope_dict[i])
        return result

if __name__ == "__main__":
    root = Node(8) 
    root.left = Node(3) 
    root.right = Node(10) 
    root.left.left = Node(1) 
    root.left.right = Node(6) 
    root.right.right = Node(14) 
    root.right.right.left = Node(13) 
    root.left.right.left = Node(4) 
    root.left.right.right = Node(7)
    DT = DiagonalTraversal()
    print(DT.diagonal_traversal(root))
        