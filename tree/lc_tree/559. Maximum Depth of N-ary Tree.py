"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        max_depth = 0
        while stack:
            node, level = stack.pop()
            max_depth = max(max_depth, level)
            if node:
                for child in node.children:
                    stack.append((child, level + 1))
        return max_depth
