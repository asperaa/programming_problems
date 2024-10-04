# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        queue = deque()
        queue.append(root)
        queue.append(None)
        result = []
        prev = -1
        
        while queue:
            node = queue.popleft()
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node.val
            else:
                if queue:
                    queue.append(None)
                result.append(prev)
        return result
            
        
        
