# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.parent_and_depth = {}
        
    def cousins_dfs(self, root, x, y, curr_depth):
        if not root:
            return None
        
        if root.left:
            if root.left.val == x:
                self.parent_and_depth[x] = (root.val, curr_depth + 1)
            elif root.left.val == y:
                self.parent_and_depth[y] = (root.val, curr_depth + 1)
            self.cousins_dfs(root.left, x, y, curr_depth + 1)
        
        
        if root.right:
            if root.right.val == x:
                self.parent_and_depth[x] = (root.val, curr_depth + 1)
            elif root.right.val == y:
                self.parent_and_depth[y] = (root.val, curr_depth + 1)
            self.cousins_dfs(root.right, x, y, curr_depth + 1)
    

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        self.cousins_dfs(root, x, y, 0)
        if self.parent_and_depth[x][0] != self.parent_and_depth[y][0] and self.parent_and_depth[x][1] == self.parent_and_depth[y][1]:
            return True
        else:
            return False
        
