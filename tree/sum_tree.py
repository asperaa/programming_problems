"""Given tree is sum tree or not.A SumTree is a Binary Tree where value of every node x is equal 
to sum of nodes present in its left subtree and right subtree of x. An empty tree is SumTree 
and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree."""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def sum_tree(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True

    root_sum = 0
    if root.left:
        root_sum += root.left.val
    if root.right:
        root_sum += root.right.val
    if root_sum == root.val:
        left_result = sum_tree(root.left)
        right_result = sum_tree(root.right)
        if left_result and right_result:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(2)
    # root.right.right = TreeNode(3)
    print(sum_tree(root))

