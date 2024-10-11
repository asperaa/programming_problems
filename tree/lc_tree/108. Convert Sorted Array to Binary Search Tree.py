# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convert(self, arr, l, r):
        if l > r:
            return None
        mid = (l+r) // 2
        node = TreeNode(arr[mid])
        node.left = self.convert(arr, l, mid-1)
        node.right = self.convert(arr, mid+1, r)
        return node
                
    
    def sortedArrayToBST(self, arr):
        return self.convert(arr, 0, len(arr)-1)    