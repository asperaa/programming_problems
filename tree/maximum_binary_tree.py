"""654. Make a maximum binary tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def max_tree(arr):
    if not arr:
        return None
    length = len(arr)    
    max_index = arr.index(max(arr))
    maxx = max(arr)
    root = TreeNode(maxx)
    if max_index == 0:
        left_arr = []
    else:
        left_arr = arr[0:max_index]
    if max_index == length - 1:
        right_arr = []
    else:
        right_arr = arr[max_index+1:length]
    root.left = max_tree(left_arr)
    root.right = max_tree(right_arr)
    return root

if __name__ == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    root = max_tree(arr)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.left.right.val, root.left.right.right.val)