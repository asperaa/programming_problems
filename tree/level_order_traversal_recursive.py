"""Level order traversal in a tree. Recursive"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class LevelOrder:
    def __init__(self):
        self.levels = []
    
    def level_order_util(self, root, level):
        if len(self.levels) == level:
            self.levels.append([])
        
        self.levels[level].append(root.val)

        if root.left:
            self.level_order_util(root.left, level + 1)
        if root.right:
            self.level_order_util(root.right, level + 1)


    def level_order(self, root):
        if not root:
            return self.levels
        self.level_order_util(root, 0)
        return self.levels

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    LevelOrder_ = LevelOrder()
    print(LevelOrder_.level_order(root))
        
        