"""Sum root to leaf numbers"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class SumRootLeaf:
    def __init__(self):
        self.final_sum = 0
    
    def dfs(self, root, curr_num):
        if not root:
            return None
        curr_num = curr_num*10 + root.val
        self.dfs(root.left, curr_num)
        self.dfs(root.right, curr_num)
        if not root.left and not root.right:
            self.final_sum += curr_num
        return None
    
    def root_to_leaf_sum(self, root):
        if not root:
            return None
        self.dfs(root, 0)
        return self.final_sum

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    SumRootLeaf = SumRootLeaf()
    print(SumRootLeaf.root_to_leaf_sum(root))

        
        
