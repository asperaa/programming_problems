# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.appendleft(root)
        queue.appendleft(None)
        row_max = float('-inf')
        
        while queue:
            node = queue.pop()
            if node:
                if node.left is not None:
                    queue.appendleft(node.left)
                if node.right is not None:
                    queue.appendleft(node.right)
                row_max = max(row_max, node.val)
            else:
                result.append(row_max)
                row_max = float('-inf')
                if queue:
                    queue.appendleft(None)
        return result
            
        
        