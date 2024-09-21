# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def dfs(self, root, result):
        if not root:
            return -1
        left_height = self.dfs(root.left, result)
        right_height = self.dfs(root.right, result)
        curr_height = 1 + max(left_height, right_height)
        if curr_height == len(result):
            result.append([])
        result[curr_height].append(root.val)
        return curr_height
    
    
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.dfs(root, result)
        return result