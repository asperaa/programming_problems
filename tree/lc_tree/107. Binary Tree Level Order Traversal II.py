# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        result = deque()
        queue = deque()
        sub_result = []
        
        queue.append(root)
        queue.append(None)
        
        while queue:
            node = queue.popleft()
            if node:
                if node.left is not None:
                    sub_result.append(node.left)
                if node.right is not None:
                    sub_result.append(node.right)
                sub_result.append(node.val)
            else:
                result.appendleft(sub_result)
                sub_result = []
                if queue:
                    queue.append(None)
        return result
        