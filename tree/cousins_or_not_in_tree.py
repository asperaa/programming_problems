"""Cousins or not in a binary tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Cousins:
    def __init__(self):
        self.parent_depth = dict()
    
    def cousins_util(self, root, x, y, curr_depth):
        if not root:
            return None

        if root.left:
            if root.left.val == x:
                self.parent_depth[x] = (root.val, curr_depth + 1)
            elif root.left.val == y:
                self.parent_depth[y] = (root.val, curr_depth + 1)

            self.cousins_util(root.left, x, y, curr_depth + 1)
        if root.right:
            if root.right.val == x:
                self.parent_depth[x] = (root.val, curr_depth + 1)

            elif root.right.val == y:    

                self.parent_depth[y] = (root.val, curr_depth + 1)
            self.cousins_util(root.right, x, y, curr_depth + 1)
        return None
    
    def cousins(self, root, x, y):
        if not root:
            return False
        self.parent_depth[root.val] = (0, 0)
        self.cousins_util(root, x, y, 0)
        if self.parent_depth[x][0] != self.parent_depth[y][0] and self.parent_depth[x][1] == self.parent_depth[y][1]:
            return True
        else:
            return False

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    Cousins = Cousins()
    print(Cousins.cousins(root, 4, 5))
        
        
