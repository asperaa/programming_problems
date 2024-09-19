# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_traversed = []
        
        if root:
            queue = []
            queue.append(root)
            
            while(len(queue)!=0):
                tree_node = queue.pop(0)
                
                level_order_traversed = 
            
        