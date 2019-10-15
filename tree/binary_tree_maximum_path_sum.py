"""Binary Tree Maximum Path Sum"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MaximumPathSum:
    def __init__(self):
        self.max_sum = float('-inf')
    
    def dfs(self, root):
        if not root:
            return 0
        left_sum  = max(0, self.dfs(root.left))
        right_sum = max(0, self.dfs(root.right))

        self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)
        
        return max(root.val + left_sum, root.val + right_sum)

    def max_path_sum(self, root):
        if not root:
            return 0
        self.dfs(root)
        return self.max_sum

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    MaximumPathSum = MaximumPathSum()
    print(MaximumPathSum.max_path_sum(root))