# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.is_sum = False                     # maintain the status of the target sum
    
    def dfs_util(self, root, target, curr_sum):
        if not root:
            return
        curr_sum += root.val                       # maintain the curr_sum
        self.dfs_util(root.left, target, curr_sum)  # traverse left subtrees
        self.dfs_util(root.right, target, curr_sum) # traverse right subtrees
        if not root.left and not root.right: # make sure that we are at the root
            if curr_sum == target: 
                self.is_sum = True 
        return None
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.dfs_util(root, target, 0)
        return self.is_sum