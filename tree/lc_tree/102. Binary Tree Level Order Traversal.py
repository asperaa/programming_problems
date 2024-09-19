# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result, sub_result = [],[]
        
        queue = deque()
        queue.appendleft(root)
        queue.appendleft(None)
        
        while queue:
            node = queue.pop()
            if node:
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
                sub_result.append(node.val)
            else:
                result.append(sub_result)
                sub_result = []
                if queue:
                    queue.appendleft(None)
        return result
        
        
            

            
        