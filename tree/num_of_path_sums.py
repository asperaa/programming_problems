"""Num of path sums in a tree. Time - O(n2). Space - O(n)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class NumPathSum:
    def __init__(self):
        self.numm = 0
    
    def dfs(self, root, sum, r_sum):
        if not root:
            return None
        r_sum += root.val
        if r_sum == sum:
            self.numm += 1
        self.dfs(root.left, sum, r_sum)
        self.dfs(root.right, sum, r_sum)
        return None
    
    def path_sum_num(self, root, sum):
        if not root:
            return None
        self.dfs(root, sum, 0)
        self.path_sum_num(root.left, sum)
        self.path_sum_num(root.right, sum)
        return None
    
    
    def final_num(self, root, sum):
        if not root:
            return 0
        self.path_sum_num(root, sum)
        return self.numm
        

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)

    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    NPS = NumPathSum()
    print(NPS.final_num(root, 22))
