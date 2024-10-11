
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def check_bal_util(root):
    if root == None:
        return (0, True)
    l_height, l_balanced = check_bal_util(root.left)
    r_height, r_balanced = check_bal_util(root.right)
    return max(l_height, r_height) + 1, l_balanced and r_balanced and abs(l_height - r_height) <= 1
    
    
    
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return check_bal_util(root)[1]