"""Maximum Binary Tree - Time Complexity - O(n2) or (nlogn), Space Complexity - O(n) or O(logn)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def get_max_index(arr, l, r):
    max_index = l
    for i in range(l, r):
        if arr[max_index] < arr[i]:
            max_index = i
    return max_index


def max_tree_util(arr, l, r):
    
    if l == r:
        return None
    max_index = get_max_index(arr, l, r)
    root = TreeNode(arr[max_index])
    root.left = max_tree_util(arr, l, max_index)
    root.right = max_tree_util(arr, max_index+1, r)
    return root

def max_tree(arr):
    return max_tree_util(arr, 0, len(arr))
if __name__  == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    root = max_tree(arr)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.left.right.val, root.left.right.right.val)